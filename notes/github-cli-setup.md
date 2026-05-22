# GitHub CLI Setup

GitHub CLI was installed locally so Codex can detect `gh`.

## Current Repo Remote

```powershell
git remote -v
```

Expected remote:

```text
origin  https://github.com/JuanERombado/bugbounty.git
```

## If Codex Still Shows GitHub CLI Unavailable

Restart Codex so the app refreshes PATH and detects:

```text
C:\Program Files\GitHub CLI\gh.exe
```

## If GitHub CLI Needs Login

Run:

```powershell
gh auth login
```

Choose:

- GitHub.com
- HTTPS
- Authenticate Git with GitHub CLI: yes
- Login with web browser

After login, verify:

```powershell
gh auth status
gh repo view JuanERombado/bugbounty
```

Regular `git push` already works for this repo, so GitHub CLI is mainly needed for Codex's built-in GitHub controls.
