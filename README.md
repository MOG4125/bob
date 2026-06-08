<img width="350" alt="IMG_3150-Photoroom" src="https://github.com/user-attachments/assets/9d1c7585-273b-4e24-8037-7455e7857aca" />

# Bob: A Minimalist Python Package Manager

**Bob** is a lightweight, command-line-first package manager for Python. It is designed to be a transparent wrapper around `pip`, providing a streamlined interface for managing project dependencies without the overhead of more complex tools.

---

## Table of Contents
1. [Features](#features)
2. [Automatic Updates](#automatic-updates)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Troubleshooting](#troubleshooting)
7. [Project Structure](#project-structure)
8. [Contribution](#contribution)
9. [License](#license)

---

## Features
* **Intuitive CLI:** Simple commands for standard tasks.
* **Auto-Updates:** Automatically checks PyPI for the latest versions of your dependencies.
* **Virtual Environment Friendly:** Built to work seamlessly within your existing Python workflows.
* **Extensible:** Minimal codebase that is easy to fork and build upon.

## Automatic Updates
`bob` takes the hassle out of dependency management. When you install or manage a package, `bob` performs a background check against the PyPI index:

1. **Version Resolution:** `bob` queries the PyPI API for the package's latest metadata.
2. **Comparison:** It compares the version you have installed against the latest release on PyPI.
3. **Smart Upgrade:** If an update is detected, `bob` automatically performs an upgrade. 

To keep your workflow efficient, `bob` uses a local cache, checking for updates at most once every 24 hours.



## Prerequisites
* **Python 3.8+**
* **pip** (bundled with standard Python installations)

## Installation
To install `bob` for local development, run the following commands in your terminal:

```bash
# 1. Clone the repository
git clone [https://github.com/yourusername/bob.git](https://github.com/yourusername/bob.git)
cd bob

# 2. Install in editable mode
pip install -e .
