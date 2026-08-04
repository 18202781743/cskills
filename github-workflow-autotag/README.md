# github-workflow-autotag

用于给 GitHub 仓库触发 `Auto Release` workflow 打 tag。

特性：

- 支持一次指定多个 `--project`
- 支持显式指定 `username`、`email`、`version`
- 默认从 `git config user.name` / `git config user.email` 读取身份信息
- 版本号不指定时，不传给 workflow，由 workflow 自行生成
- DTK 项目可以一次一起触发

示例：

```bash
python /home/repo/dev-tool/skills/github-workflow-autotag/autotag.py \
  --project dtkcommon \
  --project dtkcore \
  --project dtkgui \
  --version 6.0.12
```

或直接：

```bash
python /home/repo/dev-tool/skills/github-workflow-autotag/autotag.py \
  --project dtkcommon \
  --project dtklog \
  --project dtkcore \
  --project dtkgui \
  --project dtkwidget \
  --project dtkdeclarative \
  --project dde-qtintegration \
  --project dde-qtplatform-plugins \
  --version 6.0.12
```
