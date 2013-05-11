# coding=utf-8

from setuptools import setup, find_packages

import hazel

setup(name='Hazel',
      version='0.1',
      description='Gorgeous Static Blog System',
      author='Shunfan Du',
      author_email='i@perry.asia',
      url='https://github.com/shunfan/hazel',
      packages=find_packages(),
      include_package_data=True,
      license='MIT License',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'License :: OSI Approved :: MIT License',
          'Operating System :: MacOS',
          'Operating System :: POSIX',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.1',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
      ],
     )