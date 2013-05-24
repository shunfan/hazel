# coding=utf-8
import os
import yaml
import shutil
import urllib2
import fileinput

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
    default_template_path = get_path(g.hazel_path, 'default', 'limestone')
    try:
        shutil.copytree(default_template_path, get_path(os.getcwd(), 'templates', 'limestone'))
        with indent(2, quote='>'):
            puts('default template was installed successfully.')
    except:
        puts(colored.yellow('Install default template fail, check if the default template has been installed.'))

def install(template):
    load_base()
    original_path = os.getcwd()
    templates = urllib2.urlopen('https://raw.github.com/shunfan/hazel/master/templates.yml').read()
    templates = yaml.load(templates)
    try:
        git_template = templates[template]
        os.chdir(g.path.templates)
        os.system('git clone %s' % git_template)
        try:
            for line in fileinput.input(get_path(original_path, 'config.yml', inplace=True):
                print '%d: %s' % (fileinput.filelineno(), line)
            puts(colored.green('Successfully configured the template option.'))
        except:
            puts(colored.red('Configure the template fail.'))
        puts(colored.green('Template is installed properly.'))
    except:
        puts(colored.red('Template %s is not found or installed properly.' % template))

def init():
    try:
        puts('Start initiating...')
        default_mkdir()
        default_config()
        install_default_template()
        puts(colored.green('Initiating process is done.'))
    except:
        puts(colored.red('Initiate fail...'))
