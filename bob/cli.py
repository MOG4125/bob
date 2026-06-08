import argparse
import subprocess
import sys
import json
import urllib.request
import os
import time

def check_for_updates(package_name):
    """Checks PyPI and upgrades if a new version exists (once per 24 hours)."""
    cache_file = ".bob_update_cache"
    
    # 24-hour interval in seconds
    if os.path.exists(cache_file):
        if (time.time() - os.path.getmtime(cache_file)) < 86400:
            return

    try:
        url = f"https://pypi.org/pypi/{package_name}/json"
        with urllib.request.urlopen(url, timeout=2) as response:
            data = json.loads(response.read().decode())
            latest_version = data["info"]["version"]
            print(f"--- bob: Checking for updates for {package_name} ---")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package_name])
            # Update cache timestamp
            with open(cache_file, "w") as f:
                f.write(str(time.time()))
    except Exception:
        pass 

def install(package):
    print(f"--- bob: Installing {package} ---")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    check_for_updates(package)

def list_packages():
    print("--- bob: Installed packages ---")
    subprocess.check_call([sys.executable, "-m", "pip", "list"])

def main():
    parser = argparse.ArgumentParser(description="Bob: A simple Python package manager")
    subparsers = parser.add_subparsers(dest="command")

    install_parser = subparsers.add_parser("install")
    install_parser.add_argument("package", help="Name of the package")
    subparsers.add_parser("list")

    args = parser.parse_args()

    if args.command == "install":
        install(args.package)
    elif args.command == "list":
        list_packages()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
