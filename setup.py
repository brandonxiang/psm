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
KEYWORDS = "python source package"
AUTHOR = "brandonxiang"
AUTHOR_EMAIL = "1542453460@qq.com"
URL = "http://www.jianshu.com/users/64467c788eb7"
VERSION = "0.3.0"
LICENSE = "MIT"
 
setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.5',
    py_modules=['psm'],
    keywords = KEYWORDS,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = URL,
    license = LICENSE,
    install_requires=[
        'docopt>=0.6.2',
        'configparser>=7.1.0'
    ],
    scripts=['psm'],
    # packages = PACKAGES,
    include_package_data=True,
    zip_safe=True,
)