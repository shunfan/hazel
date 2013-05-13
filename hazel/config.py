# coding=utf-8
import os
import shutil

from clint.textui import puts, indent, colored
from hazel.utils import safe_mkdir, force_mkdir, create, write


def default_mkdir():
    safe_mkdir('posts')
    safe_mkdir('site')
    safe_mkdir('templates')
    with indent(2, quote='>'):
        puts('all directories were initiated successfully.')

def install_default_template():
    hazel_path = os.path.abspath(os.path.dirname(__file__))
    default_template_path = os.path.join(hazel_path, 'default_template', 'hazel')
    try:
        shutil.copytree(default_template_path, os.path.join(os.getcwd(), 'templates', 'hazel'))
        with indent(2, quote='>'):
            puts('default template was initiated successfully.')
    except:
        puts(colored.yellow('Initiate default template fail, check if hazel is installed correctly.'))

def init():
    try:
        puts('Start initiating...')
        default_mkdir()
        install_default_template()
        config = '''site_name: A blog powered by hazel\ntemplate: hazel\nindex_post: 3'''
        create('config.yml', config)
        puts(colored.green('Initiating process is done.'))
    except:
        puts(colored.red('Initiate fail...'))
