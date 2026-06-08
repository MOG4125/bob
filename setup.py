from setuptools import setup, find_packages

setup(
    name="bob-pkg",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "bob=bob.cli:main",
        ],
    },
)
