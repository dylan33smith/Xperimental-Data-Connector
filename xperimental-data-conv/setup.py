#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(name='xperimental-data-conv',
      version='1.0.0-alpha-9',
      url='https://github.com/SynBioDex/Experimental-Data-Convertor',
      license='BSD 3-clause',
      maintainer='Jet Mante',
      maintainer_email='jet.mante@colorado.edu',
      include_package_data=True,
      description='convert excel resources into sbol and flapjack and upload them',
      packages=find_packages(include=['xperimental_data_conv']),
      long_description=open('README.md').read(),
      install_requires=['pyflapjack==1.0.5',
                        'pandas==1.3.3',
                        'openpyxl==3.0.9'],
      zip_safe=False)
