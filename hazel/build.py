# coding=utf-8

import os
import re
import time
import yaml
import codecs
import shutil
import datetime
import markdown

from operator import itemgetter
from hazel.utils import ObjectDict
from clint.textui import puts, indent, colored
from jinja2 import Template, Environment, FileSystemLoader


class Post(ObjectDict):
    def __init__(self):
        self.date = []


def path_to_file(directory, filename):
    return os.path.join(g.config['path'], directory, filename)


def path_to_directory(directory):
    return os.path.join(g.config['path'], directory)


def path_to_template_assets():
    return os.path.join(g.config['path'], 'templates', g.config['template'], 'assets')


def render_template(template, **content):
    env = Environment(loader=FileSystemLoader(g.template))
    template = env.get_template(template)
    return template.render(content)


def write(filename, content):
    with codecs.open(path_to_file('site', filename + '.html'), mode='w', encoding='utf-8') as f:
        f.write(content)


def load_yaml():
    with open('config.yaml', 'r') as f:
        g.config = yaml.load(f.read())


def load_path():
    g.template = os.path.join(g.config['path'], 'templates', g.config['template'])
    g.template_assets = os.path.join(g.template, 'assets')
    g.site = path_to_directory('site')
    g.site_assets = os.path.join(g.site, 'assets')


def read_post(filename):
    post = Post()
    with codecs.open(path_to_file('posts', filename), mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        if lines[0].startswith('---'):
            lines.pop(0)
        for l, line in enumerate(lines):
            if line.startswith('---'):
                meta = yaml.load(''.join(lines[:l]))
                post.title = meta['title']
                post.slug = re.split('\.+', filename)[0]
                post.date = meta['date'].strftime('%Y-%m-%d')
                post.content = markdown.markdown(''.join(lines[l + 1:]))
                g.posts.append(post)
                break
    html = render_template('post.html', title=post.title, slug=post.slug, date=post.date, content=post.content)
    write(re.split('\.+', filename)[0], html)


def read_posts():
    g.posts = []
    pattern = re.compile('.+\.md$', re.I)
    posts = [p for p in os.listdir(path_to_directory('posts')) if pattern.match(p)]
    if posts:
        for p in posts:
            try:
                read_post(p)
                puts('File %s is read successfully.' % p)
            except:
                puts(colored.yellow('File %s is not concord with the style of hazel document.' % p))
        g.posts = sorted(g.posts, key=itemgetter('date'), reverse=True) 
    else:
        puts(colored.red('No posts in the posts directory.'))


def build_index():
    html = render_template('index.html', posts=g.posts[:g.config['index_post']])
    write('index', html)


def build_archive():
    html = render_template('archive.html', posts=g.posts)
    write('archive', html)

def copy_assets():
    if os.path.exists(g.site_assets):
        shutil.rmtree(g.site_assets)
    shutil.copytree(g.template_assets, g.site_assets)

def build():
    g.time = time.time()
    load_yaml()
    load_path()
    read_posts()
    build_index()
    build_archive()
    copy_assets()
    puts(colored.green('Well Done! Buidng process cost %.3fs in total.' % (time.time() - g.time)))

g = ObjectDict
build()
