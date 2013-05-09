# coding=utf-8
import os
import yaml
import markdown


class Post:
    pass


def load_yaml():
    with open('config.yaml', 'r') as f:
        config = yaml.load(f.read())
    return config


def path(directory, filename):
    return os.path.join(config['path'], directory, filename)


def read_post():
    post = Post()
    with open(path('posts', 'first-post.md'), 'r') as f:
        lines = f.readlines()
        for l, line in enumerate(lines):
            if line.startswith('---'):
                post.info = yaml.load(''.join(lines[:l]))
                post.content = markdown.markdown(unicode(''.join(lines[l + 1:])))
        return post


def write(filename, content):
    with open(path('articles', filename + '.html'), 'w') as f:
        f.write(content)


config = load_yaml()
post = read_post()
write(post.info['title'], post.content)