# coding=utf-8

from setuptools import setup, find_packages

from hazel import __version__

setup(
    name='hazel',
    version=__version__,
    author='Shunfan Du',
    author_email='i@perry.asia',
    description='Gorgeous Static Blog System',
    license='MIT',
    keywords='static blog markdown',
    url='https://github.com/shunfan/hazel',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
      'console_scripts': [
        'hazel = hazel.build:generate'
      ],
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'License :: OSI Approved :: MIT Licenseh',
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