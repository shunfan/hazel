# coding=utf-8

import os
import re
import yaml
import codecs
import shutil
import markdown

from operator import itemgetter
from datetime import datetime, date, time
from clint.textui import puts, indent, colored
from jinja2 import Template, Environment, FileSystemLoader
from hazel.utils import ObjectDict, path_to_file, render_template, write, g


class Post(ObjectDict):
    pass


def load_yaml():
    with open('config.yml', 'r') as f:
        g.config = yaml.load(f.read())


def load_path():
    g.posts = os.path.join(g.config['path'], 'posts')
    g.template = os.path.join(g.config['path'], 'templates', g.config['template'])
    g.template_assets = os.path.join(g.template, 'assets')
    g.site = os.path.join(g.config['path'], 'site')
    g.site_assets = os.path.join(g.site, 'assets')
    if os.path.exists(g.site):
        shutil.rmtree(g.site)
        os.mkdir(g.site)
    else:
        os.mkdir(g.site)


def load_jinja():
    g.template = Environment(loader=FileSystemLoader(g.template))
    g.template.globals['site_name'] = g.config['site_name']


def handle_posts():
    g.archive = []
    pattern = re.compile('.+\.md$', re.I)
    posts = [p for p in os.listdir(g.posts) if pattern.match(p)]
    if posts:
        for p in posts:
            handle_post(p)
        try:
            g.archive = sorted(g.archive, key=itemgetter('date'), reverse=True)
        except:
            puts(colored.red('Archive can not be sorted, please check whether the date of post is right.'))
    else:
        puts(colored.red('No posts in the posts directory.'))


def handle_post(filename):
    post = Post()
    puts('Reading %s now...' % filename)
    with codecs.open(path_to_file(g.posts, filename), mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        if lines[0].startswith('---'):
            lines.pop(0)
        for l, line in enumerate(lines):
            if line.startswith('---') or line.startswith('\n'):
                meta = yaml.load(''.join(lines[:l]))
                meta = dict((a.lower(), b) for a,b in meta.iteritems())
                post.title = meta['title']
                post.slug = re.split('\.+', filename)[0]
                post.date = meta['date']

                if type(post.date) is datetime:
                    pass
                elif type(post.date) is date:
                    post.date = datetime.combine(post.date, time(0, 0))
                else:
                    puts(colored.red('File %s has wrong date format.' % filename))

                post.content = markdown.markdown(''.join(lines[l + 1:]))
                g.archive.append(post)
                with indent(2, quote='>'):
                    puts('read successfully.')
                break
    try:
        html = render_template('post.html', post=post, config=g.config)
        with indent(2, quote='>'):
            puts('rendered successfully.')
        try:
            write(g.site, re.split('\.+', filename)[0], html)
            with indent(2, quote='>'):
                puts('written successfully.')
        except:
            puts(colored.red('%s could not be written.' % filename))
    except:
        puts(colored.red('%s could not be rendered.' % filename))


def build_index():
    html = render_template('index.html', posts=g.archive[:g.config['index_post']], config=g.config)
    write(g.site, 'index', html)


def build_archive():
    html = render_template('archive.html', posts=g.archive, config=g.config)
    write(g.site, 'archive', html)

def copy_assets():
    shutil.copytree(g.template_assets, g.site_assets)

def generate():
    try:
        load_yaml()
        load_path()
        load_jinja()
        handle_posts()
        build_index()
        build_archive()
        copy_assets()
        puts(colored.green('Complete.'))
    except:
        puts(colored.red('Loaded fail, please check if all files are in the directory.'))
