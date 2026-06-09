import sys
import os

def run_pip(args, dry_run=False):
    """Internal helper to execute pip with performance-optimized flags."""
    # Build the base command
    cmd = [sys.executable, "-m", "pip"] + args + [
        "--disable-pip-version-check", 
        "--no-input",
        "--quiet"
    ]
    
    # Handle Ghost Mode (Dry Run)
    if dry_run:
        cmd.append("--dry-run")
        print("--- Ghost Mode: Dry Run (No changes will be made) ---")

    import subprocess # Lazy loading
    subprocess.check_call(cmd)

def install(package, dry_run=False):
    print(f"Installing {package}...")
    run_pip(["install", package], dry_run=dry_run)

def uninstall(package):
    print(f"Uninstalling {package}...")
    run_pip(["uninstall", "-y", package])

def sync():
    if not os.path.exists("requirements.bob"):
        print("Error: requirements.bob file not found.")
        return

    print("Synchronizing environment (optimized)...")
    run_pip(["install", "-r", "requirements.bob", "--upgrade"])
    print("Sync complete.")

def check():
    """Checks for outdated packages using Ghost Mode logic."""
    if not os.path.exists("requirements.bob"):
        print("Error: requirements.bob file not found.")
        return
    
    print("Checking dependencies for updates...")
    run_pip(["list", "--outdated", "--format=columns"])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: bob <command> [args]")
        sys.exit(1)
        
    command = sys.argv[1]
    
    # Logic for commands
    if command == "install":
        # Check if user requested dry run: bob install <pkg> --dry-run
        is_dry = "--dry-run" in sys.argv
        package = sys.argv[2] if len(sys.argv) > 2 else None
        if package:
            install(package, dry_run=is_dry)
    elif command == "uninstall":
        uninstall(sys.argv[2])
    elif command == "sync":
        sync()
    elif command == "check":
        check()
