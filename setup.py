from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md")) as fp:
    long_description = fp.read()

setup(
    name="mkjsfiddle",
    version="0.2.0",
    description="An MkDocs plugin that lets you edit code fences in JSFiddle.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stadiamaps/mkjsfiddle",
    author="Stadia Maps",
    author_email="info@stadiamaps.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="mkdocs jsfiddle plugin",
    license="MIT",
    packages=["mkjsfiddle"],
    python_requires=">=3.6, <4",
    install_requires=["mkdocs"],
    extras_require={"test": ["pytest"],},
    entry_points={"mkdocs.plugins": ["jsfiddle = mkjsfiddle.plugin:JSFiddlePlugin",],},
)
