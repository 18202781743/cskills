# Eval 测试

使用 DTK 版本 6.7.45（玲珑 runtime 6.7.0.45）进行 dry-run 测试，验证各命令参数传递和版本推断。

## 运行

```bash
# 运行全部测试
python3 evals/test_dryrun.py all

# 单独测试某个命令
python3 evals/test_dryrun.py version      # 版本推断（从 deb 仓库解析）
python3 evals/test_dryrun.py crp-pack     # CRP 打包
python3 evals/test_dryrun.py build-repo   # 制作更新仓库
python3 evals/test_dryrun.py update-repo  # 修改 yaml + PR
python3 evals/test_dryrun.py build-layer  # 构建玲珑 Layer
python3 evals/test_dryrun.py push-layer   # N8N 推送
```

## 测试内容

- **版本推断**: 从 deb 仓库解析 dtkcore 版本，映射为玲珑 runtime 格式（如 `libdtk6core_6.7.45_amd64.deb` → 玲珑 `6.7.0.45`）
- **crp-pack**: 验证 `--version`、`--topic`、`--branch`、`--archs`、`--branch-id` 等参数传递
- **build-repo**: 验证 `--repo-id` 参数和 URL 生成
- **update-repo**: 验证 `--version` 和 `--deb-repo` 参数
- **build-layer**: 验证 `--repo-url` 和 `--repo-branch` 参数
- **push-layer**: 验证 `--layer-url` 参数

所有测试在 `--dry-run` 模式下执行，不触发实际 Jenkins/CRP/GitHub 操作。

---

# 真实环境测试 (Real Eval)

在真实环境（或 staging 环境）中分步骤执行，验证每个环节的实际行为。
**⚠️ 注意：真实测试会触发实际的 CRP/Jenkins/GitHub 操作，请确认环境安全后再执行。**

## 运行

```bash
# 运行全部真实测试（需按提示逐步确认）
python3 evals/test_real.py all

# 单独测试某个步骤
python3 evals/test_real.py step1   # CRP 打包
python3 evals/test_real.py step2   # 制作更新仓库
python3 evals/test_real.py step3   # 修改 yaml + PR
python3 evals/test_real.py step4   # 构建玲珑 Layer
python3 evals/test_real.py step5   # N8N 推送
```

## 测试设计

### Step 1: CRP 打包 (crp-pack)

**任务**: 在 CRP 平台创建 DTK 项目的打包实例。

**检验要点**:
1. CRP 认证成功（首次输入 OA/LDAP 账号密码，后续使用缓存 token）
2. 能正确搜索到主题 "玲珑runtime dtk版本更新"
3. 能正确搜索到 DTK 项目（dtkcore-v25, dtkgui-v25 等，含 `-v25` 后缀）
4. 能列出 `upstream/master` 分支的提交信息
5. 创建打包实例成功（HTTP 200）
6. 同一 topic 下重复创建时，能正确删除旧实例再创建新实例

**预期结果**: CRP 返回打包实例 ID，实例状态为构建中。

**验证命令**:
```bash
python3 scripts/linglong-update.py crp-pack --version 6.7.45 --topic "玲珑runtime dtk版本更新" --branch "crimson-testing"
```

---

### Step 2: 制作更新仓库 (build-repo)

**任务**: 触发 Jenkins `runtime-repo-update` job，生成 deb 更新仓库。

**检验要点**:
1. Jenkins 认证成功（首次输入用户名密码，后续使用缓存）
2. Job 触发成功（HTTP 200/201/302）
3. 能正确获取构建编号
4. 构建已触发但不等待（使用 `check-repo` 轮询）
5. `check-repo` 构建成功后提取仓库 URL
6. URL 格式正确：`http://10.20.64.92:8080/crimson_runtime/stable_<repo-id>/`

**预期结果**: Jenkins job 触发成功，`check-repo` 轮询后返回有效仓库 URL。

**验证命令**:
```bash
python3 scripts/linglong-update.py build-repo --repo-id test20260722
```

---

### Step 3: 修改 yaml + PR (update-repo)

**任务**: 修改 org.deepin.runtime 和 org.deepin.runtime.webengine 的 linglong.yaml，创建 PR 并等待合并。

**检验要点**:
1. `gh auth status` 通过，GitHub 认证有效
2. 自动 clone 两个仓库到 `~/.cache/linglong-runtime-update/repos/`
3. 创建/复用分支 `update/linglong-runtime`
4. webengine 仓库正确应用 `assets/webengine.patch` 补丁
5. `linglong.yaml` 中版本号正确更新为玲珑格式（如 `6.7.0.45`，DTK `X.Y.Z` → 玲珑 `X.Y.0.Z`）
6. `linglong.yaml` 中仓库 URL 正确更新
7. `daily.bash` 执行成功，yaml 文件内容被更新
8. git commit 信息包含版本号和仓库地址
9. `gh pr create` 成功创建 PR
10. PR 标题和 body 格式正确
11. （可选）PR 能被正常合并

**预期结果**: 两个仓库各产生一个 PR，PR 内容正确。

**验证命令**:
```bash
python3 scripts/linglong-update.py update-repo --version 6.7.0.45 --deb-repo http://10.20.64.92:8080/crimson_runtime/stable_test20260722/
```

---

### Step 4: 构建玲珑 Layer (build-layer)

**任务**: 触发 Jenkins `linglong-runtime-build` job，构建玲珑 layer。

**检验要点**:
1. Job 触发成功，传入正确的 `REPO_URL` 和 `REPO_BRANCH` 参数
2. 能正确获取构建编号
3. `build-layer` 仅触发构建，使用 `check-build` 轮询
4. 轮询到构建成功（result == "SUCCESS"）
5. 从控制台输出中可提取构建产物的 layer URL

**预期结果**: Jenkins job 触发成功，`check-build` 轮询确认构建成功。

**验证命令**:
```bash
python3 scripts/linglong-update.py build-layer --repo-url github.com/linglongdev/org.deepin.runtime --repo-branch main
```

---

### Step 5: N8N 推送 (push-layer)

**任务**: 提交 N8N 表单，触发 Jenkins push job 将 layer 推送到玲珑仓库。

**检验要点**:
1. N8N 表单 URL 可访问
2. 能正确提示用户手动提交 N8N 表单
3. 用户确认后，触发 `linglong-runtime-push-to-old` job（传入 `LAYER_URL` 参数）
4. 用户确认后，触发 `linglong-runtime-push-to-test` job（传入 `LAYER_URL` 参数）
5. 两个 push job 都能正常触发并返回构建编号
6. 能轮询 push job 状态直到完成

**预期结果**: push-to-old 和 push-to-test 均构建成功。

**验证命令**:
```bash
python3 scripts/linglong-update.py push-layer --layer-url https://jenkins.cicd.getdeepin.org/view/dtk/job/linglong-runtime-build/205/
```


