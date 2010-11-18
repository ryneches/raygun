#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    print '(WARNING: importing distutils, not setuptools!)'
    from distutils.core import setup

setup(name='raygun',
      version='0.1',
      description='A simple wrapper for BLASTN',
      author='Russell Neches',
      author_email='ryneches@ucdavis.edu',
      url='',
      packages=['raygun', 'raygun.tests'],
      package_data={'raygun.tests': ['stap_16S.fa', 'query.fa']},
      license='BSD',
      test_suite = 'nose.collector'
      )
