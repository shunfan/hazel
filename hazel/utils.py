# coding=utf-8
from __future__ import with_statement
import os
import codecs
import shutil


class ObjectDict(dict):
    # Copied from the source code of tornado
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        self[name] = value


def path_to_file(directory, filename):
    return os.path.join(directory, filename)


def render_template(template, **content):
    template = g.template.get_template(template)
    return template.render(content)


def safe_mkdir(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)


def force_mkdir(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
        os.mkdir(directory)
    else:
        os.mkdir(directory)


def create(file_path, content):
    with codecs.open(file_path, mode='w', encoding='utf-8') as f:
        f.write(content)


def write(directory, filename, content):
    create(path_to_file(directory, filename), content)


g = ObjectDict