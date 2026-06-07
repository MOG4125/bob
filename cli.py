import argparse
import subprocess
import sys

def install(package):
    print(f"--- bob: Installing {package} ---")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def list_packages():
    print("--- bob: Installed packages ---")
    subprocess.check_call([sys.executable, "-m", "pip", "list"])

def main():
    parser = argparse.ArgumentParser(description="Bob: A simple Python package manager")
    subparsers = parser.add_subparsers(dest="command")

    # Install command
    install_parser = subparsers.add_parser("install")
    install_parser.add_argument("package", help="Name of the package")

    # List command
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
