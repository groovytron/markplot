from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="markplot",
    version="0.1.0",
    description="Simple script generating plots and csv file from your"
    " project's journals",
    long_description=long_description,
    url="https://github.com/groovytron/markplot",
    author="Julien M'Poy",
    author_email="julien.mpoy@he-arc.ch",
    license="GPL-3.0+",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: GNU General Public"
        " License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3.6",
    ],
    keywords="overview feedback work",
    py_modules=["markplot"],
    python_requires=">=3",
    install_requires=[
        "Click",
        "numpy",
        "matplotlib",
    ],
    entry_points="""
        [console_scripts]
        markplot=markplot:cli
    """, )
