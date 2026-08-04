---
name: github-workflow-autotag
description: Use when triggering GitHub Auto Release workflows for one or more repositories, optionally overriding username, email, or version. Supports batching DTK projects in one run.
---

# GitHub Workflow AutoTag

## Overview

Triggers the GitHub `Auto Release` workflow for one or more repositories. The skill supports:

- Specifying one or more project names
- Optionally overriding `username`, `email`, and `version`
- Falling back to local `git config user.name` and `git config user.email`
- Using the workflow-generated version when no version is provided
- Automatically finding the release PR and requesting reviews from the most active maintainer + current user

Implementation is intentionally kept in a single Python file.

## When to Use

**Use when:**
- You need to trigger repository tag workflows from GitHub Actions
- You may need to trigger multiple repositories together
- You want defaults from local git identity

**Trigger phrases:**
- "给 dtkcommon 触发 auto release"
- "给 dtkcommon/dtkcore/dtkgui 打 tag"
- "给 dtk 打 tag"
- "触发 dtkcommon 和 dtkwidget 的 auto release"
- "给某项目指定版本打 tag"

**Do NOT use when:**
- You need to bump `debian/changelog` and submit a PR
- The workflow is not `Auto Release`

## Quick Reference

| Operation | Command | Behavior |
|-----------|---------|----------|
| Trigger one project | `python github-workflow-autotag/autotag.py --project dtkcommon` | Triggers one repo |
| Trigger multiple projects | `python github-workflow-autotag/autotag.py --project dtkcommon --project dtkcore --project dtkgui` | Triggers multiple repos |
| Comma-separated projects | `python github-workflow-autotag/autotag.py --project dtkcommon,dtkcore,dtkgui` | Triggers multiple repos |
| Override identity | `python github-workflow-autotag/autotag.py --project dtkcommon --username "Alice" --email "alice@example.com"` | Overrides git config |
| Specify version | `python github-workflow-autotag/autotag.py --project dtkcommon --version 6.0.12` | Passes version to workflow |

## Workflow

### Step 1: Resolve Projects

The user must provide one or more `--project <value>`.

Each project is resolved to `linuxdeepin/<project>`.

For DTK usage, the user can batch multiple DTK repositories in one run, for
example:

- `dtkcommon`
- `dtkcore`
- `dtkgui`
- `dtkwidget`

Special rule:

- When the user says `dtk`, the skill layer should expand it into these 8
  projects before calling `autotag.py`:
  `dtkcommon`, `dtklog`, `dtkcore`, `dtkgui`, `dtkwidget`,
  `dtkdeclarative`, `dde-qtintegration`, `dde-qtplatform-plugins`

### Step 2: Resolve Identity

The skill resolves identity in this order:

1. CLI arguments `--username` / `--email`
2. `git config user.name`
3. `git config user.email`

If `username` or `email` cannot be resolved, the skill fails with a clear message.

### Step 3: Trigger Workflow

It runs:

```bash
gh workflow run "Auto Release" \
  --repo linuxdeepin/dtkcommon \
  -F name="Your Name" \
  -F email="you@example.com" \
  -F version="6.0.12"
```

If `version` is omitted, that field is not sent, so the workflow can generate its
own version.

### Step 4: Post-run collection and notification

After the workflow run completes (or reaches a terminal state), the skill will:

1. Query the workflow run status and conclude whether it `success` or `failure`.
2. If the run succeeded, inspect the target repository for newly created tags and releases (via `gh release list` and `git ls-remote --tags`).
3. Find related Pull Requests that correspond to the release branch (commonly `release-<version>` or the branch used by the workflow). This is done with `gh pr list` filtering by head branch name or recent PRs with titles like `Release <version>`.
4. Package a notification payload containing:
   - workflow run id, status, conclusion, run URL
   - generated tag name(s) (if any) and release URL(s)
   - PR number(s) and URL(s) that correspond to the tag/release
   - commit SHA the release was built from
5. Send the notification back to the operator (via the assistant channel) so the user receives the tag/release and PR links automatically.

Notes and error handling:
- If the workflow doesn't produce a release/tag (some workflows only publish artifacts), the skill will still report run conclusion and suggest next steps.
- If multiple tags/releases are created, all discovered tags/releases will be listed.
- PR matching prefers exact head branch match; when ambiguous the skill will include candidates and let the user pick.

## Requirements

```bash
sudo apt install gh
gh auth login
git config user.name "Your Name"
git config user.email "you@example.com"
```

## Output

The script prints JSON:

```json
{
  "success": true,
  "msg": "已处理 3 个项目",
  "projects": [
    {
      "success": true,
      "project": "dtkcommon",
      "repo": "linuxdeepin/dtkcommon",
      "actions_url": "https://github.com/linuxdeepin/dtkcommon/actions"
    }
  ]
}
```
