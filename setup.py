# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="lupon",
    version='0.3.1',
    url='https://www.lupon.ch',
    description='',
    author='Florian Rindlisbacher',
    author_email='florian.rindlisbacher@students.bfh.ch',
    packages=["lupon"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'Flask-Babel',
        'Flask-Cache',
        'Flask-Mail',
        'Flask-WTF',
        'Flask-MySQLdb',
        'Flask-SQLAlchemy',
        'Flask-Login',
        'Flask-Bcrypt==0.6.0',
        'WTForms-Alchemy',
        'requests'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)