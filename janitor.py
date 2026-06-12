#!/usr/bin/env python3
import subprocess
import sys

def get_merged_branches():
    """Runs git command to find branches merged into the current branch."""
    try:
        # Run git branch --merged
        result = subprocess.run(
            ["git", "branch", "--merged"], 
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip().split('\n')
    except subprocess.CalledProcessError:
        print("❌ Error: Are you sure you are in a valid Git repository?")
        sys.exit(1)

def main():
    print("🧹 Git Janitor - Sweeping up your repo...\n" + "-"*40)
    
    raw_branches = get_merged_branches()
    
    # Clean up the output and ignore the currently active branch (starts with *)
    branches = [b.strip() for b in raw_branches if b.strip() and not b.startswith('*')]
    
    # Branches we NEVER want to accidentally delete
    protected_branches = ['main', 'master', 'develop', 'staging']
    
    # Filter out protected branches
    to_delete = [b for b in branches if b not in protected_branches]

    if not to_delete:
        print("✨ Your repository is sparkling clean! No merged branches to delete.")
        return

    print("🗑️  Found the following merged branches taking up space:")
    for b in to_delete:
        print(f"  - {b}")
    
    print("-" * 40)
    confirm = input("Do you want to safely delete these branches? [y/N]: ")
    
    if confirm.lower() in ['y', 'yes']:
        for b in to_delete:
            subprocess.run(["git", "branch", "-d", b])
        print("\n✅ Cleanup complete! Your repo is fresh.")
    else:
        print("\n🛑 Aborted. No branches were touched.")

if __name__ == "__main__":
    main()
