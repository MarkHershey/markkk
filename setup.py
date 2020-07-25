from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="markkk",
    version="0.0.2",
    author="Mark Huang",
    author_email="mark.h.huang@gmail.com",
    description="Personal Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MarkHershey/python-utils",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    python_requires=">=3.6",
)


# Classifiers ref: https://pypi.org/classifiers/
