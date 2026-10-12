# Publish and maintain ADR on GitHub

> ADR document set: **v0.1.61**. Research revisions and source/build versions below describe their original scope.

## Ongoing research increments

The repository is already public. Follow the [standard workflow](08-research/workflow.md), run `python tools/check_repository.py` and relevant source/generator checks, update current navigation/changelog, commit the scoped change, then verify the published branch head and file contents/blob identities. GitHub renders Markdown directly; no engine compilation or GitHub Pages deployment is required. Runtime work remains deferred.

The initial-import instructions below are retained for a fresh repository or local checkout.


## Option A — GitHub Desktop (no command line required)
1. Extract the GitHub-ready ZIP to a folder.
2. In **GitHub Desktop**, choose **File → Add Local Repository** and select the extracted folder.
3. If prompted, choose **Create a Repository Here** (name suggestion: `anomaly-development-reference`).
4. Commit the initial files.
5. Click **Publish repository**, choose **Public** if Demonized should be able to browse without an invite.
6. Share the repository URL and point reviewers to the root `README.md`.

## Option B — Terminal / Git (existing empty GitHub repository)
1. Create an **empty** GitHub repository (do not initialize it with README, license or .gitignore).
2. Extract this ZIP; open a terminal inside the extracted folder.
3. Run:

```bash
git init
git branch -M main
git add .
git commit -m "Publish ADR documentation"
git remote add origin https://github.com/YOUR-USER/anomaly-development-reference.git
git push -u origin main
```

Replace `YOUR-USER` with your GitHub account/organization. GitHub authentication is required.

## Important
- Do not upload the ADR ZIP itself as a single file to GitHub: GitHub will **not**
  unpack that file into browsable Markdown pages.
- You do not need GitHub Pages or a build system; GitHub renders the Markdown directly.
- Review the repo before setting it public: source notes may mention CtZ architecture or
  early research conclusions. Leave a visible work-in-progress notice.
- This repository contains **no license**; maintenance does not add one.
