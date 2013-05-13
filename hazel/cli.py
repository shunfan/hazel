# coding=utf-8
"""
Usage: hazel init...
       hazel generate
       hazel write <title>

Options: -h, --help

"""
from docopt import docopt
from hazel.config import init
from hazel.build import new_post, generate

args = docopt(__doc__)

def main():

    if args['generate']:
        generate()

    if args['init']:
        init()

    if args['write']:
        new_post(args['<title>'])
