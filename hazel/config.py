# coding=utf-8
import os
import shutil

from clint.textui import puts, indent, colored

from hazel.load import load_base
from hazel.utils import get_path, safe_mkdir, safe_copy, g


g.hazel_path = os.path.abspath(os.path.dirname(__file__))

def default_mkdir():
    load_base()
    safe_mkdir(g.path.posts)
    safe_mkdir(g.path.images)
    safe_mkdir(g.path.site)
    safe_mkdir(g.path.templates)
    with indent(2, quote='>'):
        puts('all directories were initiated successfully.')


def default_config():
    default_config_path = get_path(g.hazel_path, 'default', 'config.yml')
    safe_copy(default_config_path, get_path(os.getcwd(), 'config.yml'))

def install_default_template():
    default_template_path = get_path(g.hazel_path, 'default', 'hazel')
    try:
        shutil.copytree(default_template_path, get_path(os.getcwd(), 'templates', 'hazel'))
        with indent(2, quote='>'):
            puts('default template was initiated successfully.')
    except:
        puts(colored.yellow('Initiate default template fail, check if the default template has been installed.'))

def init():
    try:
        puts('Start initiating...')
        default_mkdir()
        default_config()
        install_default_template()
        puts(colored.green('Initiating process is done.'))
    except:
        puts(colored.red('Initiate fail...'))
