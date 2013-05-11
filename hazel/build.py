# coding=utf-8

import os
import re
import time
import yaml
import codecs
import datetime
import markdown

from hazel.utils import ObjectDict
from clint.textui import puts, indent, colored
from jinja2 import Template, Environment, FileSystemLoader


class Post(ObjectDict):
    def __init__(self):
        self.date = []


def load_yaml():
    with open('config.yaml', 'r') as f:
        g.config = yaml.load(f.read())


def path_to_file(directory, filename):
    return os.path.join(g.config['path'], directory, filename)


def path_to_directory(directory):
    return os.path.join(g.config['path'], directory)


def path_to_template():
    return os.path.join(g.config['path'], 'templates', g.config['template'])


def render_template(template, **context):
    env = Environment(loader=FileSystemLoader(path_to_template()))
    template = env.get_template(template)
    return template.render(context)


def write(filename, content):
    with codecs.open(path_to_file('site', filename + '.html'), mode='w', encoding='utf-8') as f:
        f.write(content)


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
                try:
                    post.date = meta['date'].strftime('%B %d, %Y')
                except:
                    date = meta['date'].split('-')
                    post.date = datetime.date(int(date[0]), int(date[1]), int(date[2])).strftime('%B %d, %Y')
                    puts(colored.red('Date is not exact proper in file %s, but it\'s ok.' % filename))
                post.content = markdown.markdown(''.join(lines[l + 1:]))
                post.html = render_template('post.html', title=post.title, slug=post.slug, date=post.date, content=post.content)
                if len(g.posts) <= g.config['post_per_page']:
                    g.posts.append(post)
                break
    try:
        write(re.split('\.+', filename)[0], post.html)
    except:
        pass


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
    else:
        puts(colored.red('No files in the post directory.'))


def build_index():
    html = render_template('index.html', posts=g.posts)
    write('index', html)


def build():
    g.time = time.time()
    load_yaml()
    read_posts()
    build_index()
    puts(colored.green('Well Done! Buidng process cost %.3fs in total.' % (time.time() - g.time)))

g = ObjectDict
build()
