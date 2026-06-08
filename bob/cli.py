import sys
import subprocess
import argparse
import os

def run_pip(args):
    """Helper to run pip commands safely."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip"] + args)
        return True
    except subprocess.CalledProcessError:
        return False

def install(package):
    print(f"Installing {package}...")
    run_pip(["install", package])

def uninstall(package):
    print(f"Uninstalling {package}...")
    # -y flag automatically confirms the uninstall
    run_pip(["uninstall", "-y", package])

def sync():
    """Syncs the environment with requirements.bob."""
    if not os.path.exists("requirements.bob"):
        print("Error: requirements.bob file not found.")
        return

    with open("requirements.bob", "r") as f:
        packages = [line.strip() for line in f if line.strip()]
    
    if not packages:
        print("requirements.bob is empty.")
        return

    print("Synchronizing environment...")
    run_pip(["install", "--upgrade"] + packages)
    print("Sync complete.")

def main():
    parser = argparse.ArgumentParser(description="Bob: Minimalist Package Manager")
    subparsers = parser.add_subparsers(dest="command")

    # Install command
    parser_install = subparsers.add_parser("install")
    parser_install.add_argument("package")

    # Uninstall command
    parser_uninstall = subparsers.add_parser("uninstall")
    parser_uninstall.add_argument("package")

    # Sync command
    subparsers.add_parser("sync")

    args = parser.parse_args()

    if args.command == "install":
        install(args.package)
    elif args.command == "uninstall":
        uninstall(args.package)
    elif args.command == "sync":
        sync()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
