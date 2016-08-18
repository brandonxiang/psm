import codecs
import os
import sys
 
from setuptools import setup, find_packages

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()
 
 
 
NAME = "psm"
PACKAGES = ["psm"]
DESCRIPTION = "Pypi Source Manager: fast switch between different Pypi Source: pypi, double, aliyun."
LONG_DESCRIPTION = open('README.md').read()
KEYWORDS = "source python package"
AUTHOR = "brandonxiang"
AUTHOR_EMAIL = "1542453460@qq.com"
URL = "http://www.jianshu.com/users/64467c788eb7"
VERSION = "0.0.10"
LICENSE = "MIT"
 
setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    py_modules=['psm'],
    keywords = KEYWORDS,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = URL,
    license = LICENSE,
    install_requires=[
        'docopt>=0.6.2',
    ],
    scripts=['psm'],
    # packages = PACKAGES,
    include_package_data=True,
    zip_safe=True,
)