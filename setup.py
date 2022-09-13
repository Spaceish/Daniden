from setuptools import setup, find_packages
import codecs
import os,sys

VERSION = '1.1516'
DESCRIPTION = 'Shhh.'

# Setting up
setup(
    name = "swap",
    version = VERSION,
    author = "me",
    author_email = "spaceydot@proton.me",
    description = DESCRIPTION,
    packages = find_packages(),
    install_requires=['pystyle==0.6']
)