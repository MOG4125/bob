from setuptools import setup

setup(
    name="bob",
    version="0.1",
    packages=["bob"],
    entry_points={
        "console_scripts": [
            "bob=bob.cli:main",
        ],
    },
)
