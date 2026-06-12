<div align="center">

# 🧹 Git Janitor

*Sweep away stale, merged branches and keep your local git environment sparkling clean.*

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=for-the-badge)](https://github.com/GIGABOIZ/git-janitor/graphs/commit-activity)
[![Open Source Love](https://img.shields.io/badge/Open%20Source-❤️-red.svg?style=for-the-badge)](https://github.com/GIGABOIZ/git-janitor)

</div>

<hr>

## 💡 The Problem
Developers are great at creating branches, but terrible at deleting them. Over time, your local repository gets cluttered with dozens of merged branches, making it hard to find what you actually need.

## ✨ The Solution
**Git Janitor** is a sleek, safe-by-default CLI utility that automatically scans your repo, identifies branches that have already been merged, and helps you safely sweep them away in seconds.

## 🚀 Key Features

- 🛡️ **Safe by Default:** Only targets branches that are 100% merged.
- 🔒 **Protected Branches:** Never touches `main`, `master`, `develop`, or `staging` to prevent accidental data loss.
- ⚡ **Lightning Fast:** Built in pure Python with zero bloated dependencies.
- ✋ **Interactive:** Always asks for your explicit confirmation before deleting anything.

---

## 🛠️ Installation

Get up and running in seconds. Install it globally directly from GitHub using `pip`:

\`\`\`bash
pip install git+https://github.com/GIGABOIZ/git-janitor.git
\`\`\`

---

## 💻 Usage

Navigate to any local Git repository in your terminal and summon the janitor:

\`\`\`bash
git-janitor
\`\`\`

**What happens next?**
1. The script scans your local git tree.
2. It prints a clean list of merged branches that are safe to delete.
3. It prompts you for a \`[y/N]\` confirmation. 
4. Boom. Clean repo. 🧹

---

<div align="center">
  <b>Built with 💻 by <a href="https://github.com/GIGABOIZ">GIGABOIZ</a></b>
</div>
