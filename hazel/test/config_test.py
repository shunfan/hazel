#coding=utf-8
import os
import porter

from pytest import raises

from hazel.config import init


def test():
    porter.mkdir('test_folder', force=True)
    os.chdir('test_folder')
    init()
