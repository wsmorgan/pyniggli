#!/usr/bin/env python
try:
    from setuptools import setup
    args = {}
except ImportError:
    from distutils.core import setup
    print("""\
*** WARNING: setuptools is not found.  Using distutils...
""")

from setuptools import setup
try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

from os import path
setup(name='pyniggli',
      version='0.0.1',
      description='Finds the niggli reduced cell',
      long_description= "" if not path.isfile("README.md") else read_md('README.md'),
      author='Wiley S. Morgan',
      author_email='wiley.s.morgan@gmail.com',
      url='https://github.com/wsmorgan/pyniggli',
      license='MIT',
      setup_requires=['pytest-runner',],
      tests_require=['pytest', 'python-coveralls'],
      install_requires=[
          "numpy",
      ],
      packages=['pyniggli'],
      include_package_data=True,
      classifiers=[
          'Development Status :: 1 - planning',
          'Intended Audience :: Science/Research',
          'Natural Language :: English',
          'Operating System :: MacOS',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.6',
      ],
     )
