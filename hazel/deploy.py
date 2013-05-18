# coding=utf-8
import os

from clint.textui import puts, indent, colored

from hazel.load import load_config
from hazel.utils import g


def rsync():
    try:
        load_config()
        cmd = "rsync -avz site {user}@{host}:{dest}".format(
            user=g.config.user,
            host=g.config.host,
            dest=g.config.dest,
        )
        os.system(cmd)
        puts(colored.green('Deploy is complete.'))
    except:
        puts(colored.red('rsync failed.'))
