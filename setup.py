# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# The current directory
with open("README.md", "r") as f:
    README = f.read()

setup(name='test-python-snap',
      version='0.1dev',
      description='This is a test snap for python applications',
      long_description=README,
      long_description_content_type="text/markdown",
      author='Muhammad Yahya & Felix Forster @ OLI Systems 2020',
      url='https://github.com/m-yahya/python-snap-tutorial.git',
      packages=['olibox_core.olibox_core.olibox_pkg',
                'olibox_core.olibox_core'],
      install_requires=['click', 'paho-mqtt', ],
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent", ],
      entry_points={
          'console_scripts': [
              'test-python-snap = olibox_core.olibox_core.olibox_core:init'
          ]
      },
      )
