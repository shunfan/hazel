# coding=utf-8

"""Usage: hazel <command>

Options: -h, --help

"""
from docopt import docopt
from hazel.build import generate

arguments = docopt(__doc__)

def main():
    if arguments['<command>'] == 'generate':
        generate()
