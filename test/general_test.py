#coding=utf-8
import os

from hazel.utils import force_mkdir


def test():
    force_mkdir('test_blog')
    os.chdir('test_blog')
    os.system('hazel init')
    os.system('hazel write test_post')
    os.system('hazel generate')
