# coding=utf-8
import sys

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

from setuptools import setup, find_packages

from hazel import __version__

setup(
    name='hazel',
    version=__version__,
    author='Shunfan Du',
    author_email='i@perry.asia',
    description='hazel: a capsule static blog generator',
    long_description=open('README.rst').read(),
    license='MIT',
    keywords='blog markdown static rsync',
    url='https://github.com/shunfan/hazel',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
      'console_scripts': [
        'hazel = hazel.cli:main'
      ],
    },
    install_requires=open("requirements.txt").readlines(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
    test_requires=['nose>=1.0'],
    test_suite='nose.collector',
    **extra
)
