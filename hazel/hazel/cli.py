# coding=utf-8
"""
Usage: hazel init...
       hazel install <template>
       hazel write <title>
       hazel generate
       hazel deploy

Options: -h, --help

"""
from docopt import docopt

from hazel.config import init
from hazel.deploy import rsync
from hazel.template import install
from hazel.generate import new_post, generate


args = docopt(__doc__)

def main():

    if args['init']:
        init()

    if args['install']:
        install(args['<template>'])

    if args['write']:
        new_post(args['<title>'])

    if args['generate']:
        generate()

    if args['deploy']:
        rsync()
