from setuptools import setup, find_packages

with open("justbuild/__init__.py", "r", encoding="utf-8") as fh:
    version = None
    short_description = None
    for line in fh:
        if line.startswith("__version__"):
            version = line.split("=")[1].strip().strip('"')
        if line.startswith("__description__"):
            short_description = line.split("=")[1].strip().strip('"')
        if version and short_description:
            break

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="justbuild",
    version=version,
    author="Sean Kruzel @ Closedloop Technologies",
    author_email="sean@closedloop.lech",
    description=short_description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/closedloop-technologies/letsgo-sh",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "lfg=justbuild.lfg_cli:app",
            "justbuild=justbuild.cli:app",
        ],
    },
)
