# 🧹 Git Janitor

Developers are great at creating branches, but terrible at deleting them. **Git Janitor** is a lightweight CLI utility that safely finds and deletes local branches that have already been merged, keeping your local environment sparkling clean.

## 🚀 Features
* **Safe by Default:** Only targets branches that have already been fully merged.
* **Protected Branches:** Never accidentally deletes `main`, `master`, `develop`, or `staging`.
* **Interactive Prompt:** Always asks for confirmation before sweeping anything away.

## 🛠️ Installation

Install it globally straight from GitHub using `pip`:

\`\`\`bash
pip install git+https://github.com/GIGABOIZ/git-janitor.git
\`\`\`

## 📖 Usage

Navigate to any of your local git repositories in your terminal and simply run:

\`\`\`bash
git-janitor
\`\`\`

The tool will scan your repository, list the branches safe for deletion, and ask for your permission to sweep them away.
