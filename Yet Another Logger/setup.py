# -*- coding: utf-8 -*-

import setuptools

with open("../README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="YALogger",
    version="1.3",
    author="Divyendu Dutta",
    author_email="connect2divyendu@gmail.com",
    description="Yet Another custom logger",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DivyenduDutta/YALogger",
    packages=setuptools.find_packages(),
	install_requires= [
		'configparser'
	],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.7",
)
