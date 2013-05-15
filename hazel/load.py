# coding=utf-8
from __future__ import with_statement
import os
import yaml

from clint.textui import puts, indent, colored

from hazel.utils import ObjectDict, get_path, force_mkdir, g, path


def load_config():
    with open('config.yml', 'r') as f:
        g.config = yaml.load(f.read())


def load_template_config():
    with open(get_path(path.template,'config.yml'), 'r') as f:
        g.template_config = yaml.load(f.read())


def load_path():
    path.posts = 'posts'
    path.template = get_path('templates', g.config['template'])
    path.template_assets = get_path(path.template, 'assets')
    path.site = 'site'
    path.site_assets = get_path(path.site, 'assets')
