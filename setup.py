# coding=utf-8
from setuptools import setup, find_packages

from hazel import __version__

setup(
    name='hazel',
    version=__version__,
    author='Shunfan Du',
    author_email='i@perry.asia',
    description='Hazel is a capsule static blog generator in Python',
    license='MIT',
    keywords='static blog markdown',
    url='https://github.com/shunfan/hazel',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
      'console_scripts': [
        'hazel = hazel.cli:main'
      ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)