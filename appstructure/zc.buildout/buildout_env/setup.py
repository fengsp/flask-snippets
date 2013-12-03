# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

name = "hello"
version = "0.1"


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name=name,
    version=version,
    description="a hello world demo",
    long_description=read('README'),
    # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[],
    keywords="",
    author="",
    author_email='',
    url='',
    license='',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Flask',
    ],
    entry_points="""
    [console_scripts]
    flask-ctl = hello.script:run

    [paste.app_factory]
    main = hello.script:make_app
    debug = hello.script:make_debug
    """,
)
