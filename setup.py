import sys

from setuptools import find_packages
from setuptools import setup

requirements = ['six']

classifiers=[
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
]


setup(
    name="Discord Username Checker",
    version='0.0.1',
    description='Discord Username Checker',
    long_description='Discord Username Checker By Hassan',
    author='yhr_h11',
    author_email='hassanradhi023@gmail.com',
    packages=find_packages(),
    license="Hassan",
    install_requires=[''],
)
