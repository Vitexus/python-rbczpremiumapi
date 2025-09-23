# coding: utf-8

from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "rbczpremiumapi"
VERSION = "1.4.0"
PYTHON_REQUIRES = ">= 3.6"
REQUIRES = [
    "urllib3 >= 2.1.0, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
    "requests",
]

setup(
    name='rbczpremiumapi',
    version='1.4.0',
    description='Core Python library for Raiffeisenbank CZ Premium API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Vítězslav Dvořák',
    author_email='info@vitexsoftware.cz',
    url='https://vitexsoftware.com/',
    packages=find_packages(),
    install_requires=REQUIRES,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    include_package_data=True,
)