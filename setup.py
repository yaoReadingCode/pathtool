#!/usr/bin/env python

# pathtool
#
# Author: Noah Gift
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages
import os,sys

version = '0.1.0'
f = open(os.path.join(os.path.dirname(__file__), 'docs', 'index.txt'))
long_description = f.read().strip()
f.close()

setup(

      name='pathtool',
      version='0.1.0',
      description='an efficient python path API',
      long_description=long_description,
      classifiers=[
              'Development Status :: 4 - Beta',
              'Intended Audience :: Developers',
              'License :: OSI Approved :: MIT License',
            ],
      author='Noah Gift',
      author_email='noah.gift@gmail.com',
      url='http://pypi.python.org/pypi/pathtool',
      download_url="http://code.google.com/p/pathtool",
      license='MIT',
      py_modules=['pathtool'],
      zip_safe=False,
      py_modules=['pathtool'],
      )
