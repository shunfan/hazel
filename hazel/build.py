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

from hazel.load import load_config, load_template_config, load_path
from hazel.utils import ObjectDict, get_path, render_template, \
                        force_mkdir, write, g, path


def load_jinja():
    g.env = Environment(loader=FileSystemLoader(path.template))
    for k,v in g.template_config.iteritems():
        g.env.globals[k] = v
    """
    site.name: the name of the site
    site.url: blog.example.com
    site.author: the author of the blog
    """
    g.env.globals['site'] = ObjectDict(g.config)


def reset():
    force_mkdir(path.site)


def handle_posts():
    g.archive = []
    pattern = re.compile('.+\.md$', re.I)
    posts = [p for p in os.listdir(path.posts) if pattern.match(p)]
    if posts:
        for p in posts:
            handle_post(p)
        try:
            g.archive = sorted(g.archive, reverse=True)
        except:
            puts(colored.red('Archive can not be sorted, please check whether the date of post is right.'))
    else:
        puts(colored.red('No posts in the posts directory.'))


def handle_post(filename):
    puts('Reading %s now...' % filename)
    with codecs.open(get_path(path.posts, filename), mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        if lines[0].startswith('---'):
            lines.pop(0)
        for l, line in enumerate(lines):
            if line.startswith('---') or line.startswith('\n'):
                """
                post.title: title of the post
                post.slug: url of the post, same as the filename
                post.date: date with personal date format
                post.standard_date: date used to order the posts
                post.content: html content of the post
                """
                post = ObjectDict(dict((a.lower(), b) for a,b in yaml.load(''.join(lines[:l])).iteritems()))
                post.slug = re.split('\.+', filename)[0]
                post.standard_date = post.date

                if type(post.date) is datetime:
                    pass
                elif type(post.date) is date:
                    post.date = datetime.combine(post.date, time(0, 0))
                else:
                    puts(colored.yellow('Post %s has wrong date format.' % filename))

                post.date = post.date.strftime(g.template_config['date_format'])
                post.content = markdown.markdown(''.join(lines[l + 1:]))
                g.archive.append(post)
                with indent(2, quote='>'):
                    puts('read successfully.')
                break
    try:
        html = render_template('post.html', post=post)
        with indent(2, quote='>'):
            puts('rendered successfully.')
        try:
            write(path.site, re.split('\.+', filename)[0] + '.html', html)
            with indent(2, quote='>'):
                puts('written successfully.')
        except:
            puts(colored.red('%s could not be written.' % filename))
    except:
        puts(colored.red('%s could not be rendered.' % filename))


def build_index():
    html = render_template('index.html', posts=g.archive[:g.template_config['index_post']])
    write(path.site, 'index.html', html)


def build_archive():
    html = render_template('archive.html', posts=g.archive)
    write(path.site, 'archive.html', html)

def copy_assets():
    shutil.copytree(path.template_assets, path.site_assets)


def new_post(filename):
    try:
        load_config()
        load_path()
        initial_content = 'title: Your post title\ndate: %s\n\nStart writing here...' % datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        write(path.posts, filename + '.md', initial_content)
        puts(colored.green('New post is written successfully.'))
    except:
        puts(colored.red('Post cannot be written.'))


def generate():
    try:
        load_config()
        load_path()
        load_template_config()
        load_jinja()
        reset()
        handle_posts()
        build_index()
        build_archive()
        copy_assets()
        puts(colored.green('Complete.'))
    except:
        puts(colored.red('Generated fail, please check if all files are in the directory.'))
