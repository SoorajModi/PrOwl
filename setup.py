#!/usr/bin/env python
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    requirements = f.read()


setup(
    name='PrOwl',
    version='0.1.0',
    description='A Reddit Bot',
    long_description=readme,
    url='https://github.com/soorajmodi/prowl',
    author='Sooraj Modi',
    author_email='soorajmodi@hotmail.com',
    license=license,
    keywords=[
        'Reddit Bot',
        'PRAW',
        'python'
    ],
    packages=find_packages(exclude=('docs', 'test', 'env')),
    include_package_data=True,
    install_requires=requirements,
)
