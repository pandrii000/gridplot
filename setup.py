import os
from pathlib import Path

import setuptools
from setuptools.command.install import install
os.system("rm -rf *.egg-info")
os.system("rm -rf dist")
os.system("rm -rf build")

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gridplot",
    version="1.0.0",
    author="Andrii Polukhin",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)
