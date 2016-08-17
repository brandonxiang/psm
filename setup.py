import codecs
import os
import sys
 
try:
    from setuptools import setup
except:
    from distutils.core import setup
def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()
 
 
 
NAME = "psm"
PACKAGES = ["psm"]
DESCRIPTION = "Pypi Source Manager: fast switch between different Pypi Source: pypi, double, aliyun."
LONG_DESCRIPTION = read("README.rst")
KEYWORDS = "source python package"
AUTHOR = "brandonxiang"
AUTHOR_EMAIL = "1542453460@qq.com"
URL = "http://www.jianshu.com/users/64467c788eb7"
VERSION = "0.0.1"
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
    keywords = KEYWORDS,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = URL,
    license = LICENSE,
    packages = PACKAGES,
    include_package_data=True,
    zip_safe=True,
)