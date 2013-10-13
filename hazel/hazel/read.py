# coding=utf-8
from __future__ import with_statement
import os
import re
import yaml
import codecs
import porter
import markdown

from operator import itemgetter
from datetime import datetime, date, time

from hazel.util import ObjectDict, g

def read_post(filename):
    with codecs.open(os.path.join('posts', filename), mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        if lines[0].startswith('---'):
            lines.pop(0)
        for l, line in enumerate(lines):
            if line.startswith('---') or line.startswith('\n'):
                """
                post.title: title of the post
                post.slug: url of the post, same as the filename
                post.date: standard datetime
                post.content: html content of the post
                """
                post = ObjectDict(dict((a.lower(), b) for a,b in yaml.load(''.join(lines[:l])).iteritems()))
                post.slug = re.split('\.+', filename)[0]

                if type(post.date) is datetime:
                    pass
                elif type(post.date) is date:
                    post.date = datetime.combine(post.date, time(0, 0))

                post.content = markdown.markdown(''.join(lines[l + 1:]))
                g.archive.append(post)
                break


def read_posts():
    g.archive = []
    pattern = re.compile('.+\.md$', re.I)
    posts = [p for p in porter.TargetDirectory('posts').files() if pattern.match(p)]
    for post in posts:
        read_post(post)
    g.archive = sorted(g.archive, key=itemgetter('date'), reverse=True)
