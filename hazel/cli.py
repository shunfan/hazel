# coding=utf-8
"""
Usage: hazel init...
       hazel write <title>
       hazel generate
       hazel deploy

Options: -h, --help

"""
from docopt import docopt

from hazel.config import init
from hazel.build import new_post, generate
from hazel.deploy import rsync

args = docopt(__doc__)

def main():

    if args['generate']:
        generate()

    if args['init']:
        init()

    if args['write']:
        new_post(args['<title>'])

    if args['deploy']:
        rsync()
