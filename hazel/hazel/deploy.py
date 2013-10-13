# coding=utf-8
from __future__ import with_statement
import os
import yaml

from hazel.load import load_config
from hazel.util import ObjectDict


def rsync():
    with open('config.yml', 'r') as f:
        config = ObjectDict(yaml.load(f.read()))

    cmd = "rsync -avz site {user}@{host}:{dest}".format(
        user=config.user,
        host=config.host,
        dest=config.dest,
    )

    os.system(cmd)
