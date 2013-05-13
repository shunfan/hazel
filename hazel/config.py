# coding=utf-8
import os
import shutil

from clint.textui import puts, indent, colored
from hazel.utils import safe_mkdir, force_mkdir, create, write


def default_mkdir():
    safe_mkdir('posts')
    safe_mkdir('site')
    safe_mkdir('templates')


def install_default_template():
    hazel_path = os.path.abspath(os.path.dirname(__file__))
    default_template_path = os.path.join(hazel_path, 'default_template', 'hazel')
    shutil.copytree(default_template_path, os.path.join(os.getcwd(), 'templates', 'hazel'))

def init():
    default_mkdir()
    install_default_template()
    config = '''site_name: A blog powered by hazel\ntemplate: hazel\nindex_post: 3'''
    create('config.yml', config)
