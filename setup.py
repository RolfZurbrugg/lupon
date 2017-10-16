# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="lupon",
    version='0.3',
    url='',
    description='',
    author='Florian Rindlisbacher',
    author_email='florian.rindlisbacher@students.bfh.ch',
    packages=["lupon"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)