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


class Post:
    def __init__(self):
        self.date = []


def load_yaml():
    with open('config.yaml', 'r') as f:
        g.config = yaml.load(f.read())


def path_to_file(directory, filename):
    return os.path.join(g.config['path'], directory, filename)


def path_to_directory(directory):
    return os.path.join(g.config['path'], directory)


def read_post(filename):
    post = Post()
    with codecs.open(path_to_file('posts', filename), mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        if lines[0].startswith('---'):
            lines.pop(0)
        for l, line in enumerate(lines):
            if line.startswith('---'):
                post.yaml = yaml.load(''.join(lines[:l]))
                post.title = post.yaml['title']
                try:
                    post.date = post.yaml['date'].strftime('%B %d, %Y')
                except:
                    date = post.yaml['date'].split('-')
                    post.date = datetime.date(int(date[0]), int(date[1]), int(date[2])).strftime('%B %d, %Y')
                    puts(colored.red('Date is not exact proper in file %s, but it\'s ok.' % filename))
                post.content = markdown.markdown(''.join(lines[l + 1:]))
                env = Environment(loader=FileSystemLoader(path_to_directory('templates')))
                template = env.get_template('post.html')
                post.html = template.render(title=post.title, date=post.date, content=post.content)
                break
        return post


def read_posts():
    pattern = re.compile('.+\.md$', re.I)
    files = [f for f in os.listdir(path_to_directory('posts')) if pattern.match(f)]
    if files:
        for f in files:
            post = read_post(f)
            try:
                write(re.split('\.+', f)[0], post.html)
                puts('File %s is read successfully.' % f)
            except:
                puts(colored.yellow('File %s is not concord with the style of hazel document.' % f))
        puts(colored.green('Well Done! Buidng process cost %.3fs in total.' % (time.time() - g.time)))
    else:
        puts(colored.red('No files in the post directory.'))


def write(filename, content):
    with codecs.open(path_to_file('site', filename + '.html'), mode='w', encoding='utf-8') as f:
        f.write(content)

def build():
    g.time = time.time()
    load_yaml()
    read_posts()


g = ObjectDict()
build()