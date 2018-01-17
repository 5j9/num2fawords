"""A setuptools based setup module."""

from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='num2fawords',
    version='1.1.dev1',
    description='A tool to convert numbers (int, float) into Persian words',
    long_description=long_description,
    url='https://github.com/5j9/num2fawords',
    author='5j9',
    author_email='5j9@users.noreply.github.com',
    license='GNU General Public License v3.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: '
        'GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Natural Language :: Persian',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing :: General',
    ],
    keywords='convert number words farsi persian',
    packages=find_packages(),
    install_requires=[
        'typing;python_version<"3.5"',
        'singledispatch;python_version<"3.4"',
    ],
)
