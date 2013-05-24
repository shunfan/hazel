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

from hazel.config import install, init
from hazel.build import new_post, generate
from hazel.deploy import rsync

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
