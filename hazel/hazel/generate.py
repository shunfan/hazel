# coding=utf-8
from __future__ import with_statement
import os
import re
import yaml
import porter

from datetime import datetime
from jinja2 import Environment, FileSystemLoader

from hazel.read import read_posts
from hazel.util import ObjectDict, render_template, write, g


class FileNotFoundError(EnvironmentError):
    pass


def reset():
    """Empty the site folder."""
    site = porter.TargetDirectory('site')
    site.empty()


def load_config():
    """Load the configuration files for global use."""
    try:
        with open('config.yml', 'r') as f:
            g.config = ObjectDict(yaml.load(f.read()))
    except OSError:
        raise FileNotFoundError("config.yml is not found.")
    try:
        with open(os.path.join('templates', g.config.template, 'config.yml'), 'r') as f:
            g.template_config = ObjectDict(yaml.load(f.read()))
    except OSError:
        raise FileNotFoundError("The config.yml of the template '%s' is not found." % g.config.template)


def load_jinja():
    """Load Jinja environment."""
    g.env = Environment(loader=FileSystemLoader(os.path.join('templates', g.config.template)))
    for k,v in g.template_config.iteritems():
        g.env.globals[k] = v
    g.env.globals['site'] = g.config


def render_template(template, **content):
    """Function for render template."""
    template = g.env.get_template(template)
    return template.render(content)


def generate_posts(archive):
    """Generate all of the posts one by one."""
    for post in archive:
        html = render_template('post.html', post=post)
        write(os.path.join('site', 'post'), post.slug + '.html', html)


def generate_pages():
    """Gnerate all the pages except post.html listed in the templates."""
    pattern = re.compile('.+\.html$', re.I)
    pages = [p for p in porter.TargetDirectory(os.path.join('templates', g.config.template)).files() if pattern.match(p)]
    for page in pages:
        if not page == 'post.html':
            html = render_template(page, posts=g.archive)
            write('site', page, html)


def copy_assets():
    """Copy the assets to the site folder."""
    porter.copy(os.path.join('templates', g.config.template, 'assets'), os.path.join('site', 'assets'))
    porter.copy(os.path.join('posts', 'images'), os.path.join('site', 'post', 'images'))


def new_post(filename):
    """Write a new post in the posts folder."""
    initial_content = 'title: Your post title\ndate: %s\n\nStart writing here...\n' % datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    write('posts', filename + '.md', initial_content)


def generate():
    reset()
    load_config()
    read_posts()
    load_jinja()
    generate_posts(g.archive)
    generate_pages()
    copy_assets()
