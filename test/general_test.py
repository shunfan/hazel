#coding=utf-8
import os

from hazel.config import init
from hazel.build import new_post, generate
from hazel.utils import force_mkdir


def test():
    force_mkdir('test_blog')
    os.chdir('test_blog')
    init()
    new_post('test_post')
    generate()