from setuptools import setup, find_packages
import os

with open('README.rst', encoding='utf-8') as f:
  readme = f.read()

with open('pypag/version.py') as f:
  version = f.readline().strip()[15:-1]

setup(
  name='pypag',
  version=version,
  description='Python 3 template parser to generate HTML from a pug/jade like syntax with Jinja2 support',
  long_description=readme,
  url='https://github.com/ducent/pypag',
  author='Julien LEICHER',
  license='GPL-3.0',
  packages=find_packages(),
  include_package_data=True,
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU Affero General Public License v3',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Topic :: Text Processing :: Markup',
  ],
  install_requires=[
    'Arpeggio~=1.9.0',
  ],
  extras_require={
    'test': [
      'nose~=1.3.7',
      'sure~=1.4.11',
      'coverage~=4.5.1',
      'Jinja2~=2.10.1',
    ],
  },
)