from setuptools import find_packages, setup

MAJOR = 0
MINOR = 0
MICRO = 16
VERSION = "%d.%d.%d" % (MAJOR, MINOR, MICRO)

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="markkk",
    version=VERSION,
    author="Mark Huang",
    author_email="mark.h.huang@gmail.com",
    description="Python convenient utilities for personal usage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MarkHershey/markkk",
    package_dir=({"": "src"}),
    packages=find_packages(where="src"),
    install_requires=["colorlog>=4.1.0"],
    extras_require={"dev": ["pytest", "tox", "wheel"]},
    # Classifiers ref: https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Framework :: tox",
        "Framework :: Pytest",
    ],
    python_requires=">=3.6",
)
