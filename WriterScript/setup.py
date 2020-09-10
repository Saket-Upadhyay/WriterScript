#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WriterScript setup."""

from setuptools import setup

__VERSION__ = "0.2.1"

if __name__ == "__main__":
    setup(
        name="writerscript",
        version=__VERSION__,
        description="A word count based Esoteric Programming Language based on logic of BrainFuck",
        license="MIT",
        keywords="esoteric programming language brainfuck x64mayhem writerscript",
        author="Saket Upadhyay",
        author_email="x64mayhem@gmail.com",
        url="https://github.com/Saket-Upadhyay/WriterScript",
        py_modules=["writerscript", "writerscript.cli", "writerscript.interpreter","writerscript.translator" ,"writerscript.generator","setup"],
        install_requires=["ply"],
        entry_points={"console_scripts": ["wscript = writerscript.cli:main"]},
        classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: Implementation :: PyPy",
        ],
    )
