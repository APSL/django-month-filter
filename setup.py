#!/usr/bin/env python
# encoding: utf-8
# --------------------------------------------------------------------------

from setuptools import setup, find_packages

version = __import__('monthfilter').__version__

setup(
    name='django-month-filter',
    version=version,
    author='Apsl',
    autor_email='info@apsl.net',
    packages=find_packages(),
    license='Apache',
    description='Django month filter for admin',
    install_requires=[],
    url='https://github.com/APSL/django-month-filter',
    classifiers=[
        'Development Status :: Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: Apache License',
        'Operation System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP'
    ],
    include_package_data=True,
    zip_safe=False
)
