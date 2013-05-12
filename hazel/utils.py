# coding=utf-8

import os
import codecs


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


def write(directory, filename, content):
    with codecs.open(path_to_file(directory, filename + '.html'), mode='w', encoding='utf-8') as f:
        f.write(content)

g = ObjectDict