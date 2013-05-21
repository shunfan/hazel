# coding=utf-8
from __future__ import with_statement
import os
import yaml

from clint.textui import puts, indent, colored

from hazel.utils import ObjectDict, get_path, g


def load_config():
    with open('config.yml', 'r') as f:
        g.config = ObjectDict(yaml.load(f.read()))


def load_base():
    g.path = ObjectDict()
    g.path.posts = 'posts'
    g.path.images = get_path(g.path.posts, 'images')
    g.path.templates = 'templates'
    g.path.site = 'site'


def load_path():
    g.path.posts = 'posts'
    g.path.images = get_path(g.path.posts, 'images')
    g.path.template = get_path('templates', g.config.template)
    g.path.template_assets = get_path(g.path.template, 'assets')
    g.path.site_post = get_path(g.path.site, 'post')
    g.path.site_images = get_path(g.path.site_post, 'images')
    g.path.site_assets = get_path(g.path.site, 'assets')


def load_template_config():
    try:
        with open(get_path(g.path.template,'config.yml'), 'r') as f:
            g.template_config = ObjectDict(yaml.load(f.read()))
    except:
        puts(colored.red('The config file in the template is not found, or the template directory doesn\'t exist.'))
