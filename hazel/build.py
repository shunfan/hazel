# coding=utf-8
from __future__ import with_statement
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
from hazel.load import load_config, load_path
from hazel.utils import ObjectDict, path_to_file, render_template, \
                        force_mkdir, write, g


class Post(ObjectDict):
    pass


def load_jinja():
    g.template = Environment(loader=FileSystemLoader(g.template))
    g.template.globals['site_name'] = g.config['site_name']


def reset():
    force_mkdir(g.site)


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
                    puts(colored.yellow('File %s has wrong date format.' % filename))

                post.content = markdown.markdown(''.join(lines[l + 1:]))
                g.archive.append(post)
                with indent(2, quote='>'):
                    puts('read successfully.')
                break
    html = render_template('post.html', post=post)
    with indent(2, quote='>'):
        puts('rendered successfully.')
    write(g.site, re.split('\.+', filename)[0] + '.html', html)
    with indent(2, quote='>'):
        puts('written successfully.')


def build_index():
    html = render_template('index.html', posts=g.archive[:g.config['index_post']])
    write(g.site, 'index.html', html)


def build_archive():
    html = render_template('archive.html', posts=g.archive)
    write(g.site, 'archive.html', html)

def copy_assets():
    shutil.copytree(g.template_assets, g.site_assets)


def new_post(filename):
    load_config()
    load_path()
    initial_content = 'title: Your post title\ndate: %s\n\nStart writing here...' % datetime.now()
    write(g.posts, filename + '.md', initial_content)


def generate():
    try:
        load_config()
        load_path()
        load_jinja()
        reset()
        handle_posts()
        build_index()
        build_archive()
        copy_assets()
        puts(colored.green('Complete.'))
    except:
        puts(colored.red('Generated fail, please check if all files are in the directory.'))
