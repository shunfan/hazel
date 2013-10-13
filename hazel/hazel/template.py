# coding=utf-8
import os
import yaml
import porter
import urllib2


def install(template):
    """Grasp templates list in GitHub and get its git address and git clone it."""
    porter.mkdir(os.path.join('templates', template), force=True)
    response = urllib2.urlopen('https://raw.github.com/shunfan/hazel/master/templates.yml').read()
    templates = yaml.load(response)
    os.chdir('templates')
    os.system('git clone %s' % templates[template])
