# coding=utf-8
import os
import yaml
import porter
import urllib2


def init():
    """Initiation foundamental folders and default config.yml for global configuration."""
    porter.mkdir('posts', ignore=True)
    porter.mkdir(os.path.join('posts', 'images'), ignore=True)
    porter.mkdir('site', ignore=True)
    porter.mkdir('site', ignore=True)

    hazel_path = os.path.abspath(os.path.dirname(__file__))
    default_config_path = os.path.join(hazel_path, 'default', 'config.yml')
    porter.copy_to(default_config_path, os.getcwd(), ignore=True)
