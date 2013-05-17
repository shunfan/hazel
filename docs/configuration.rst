Configuration
=============

If you wanna personalize your blog function or looking style, you'd better to read this documentation precisely.

General Configuration
---------------------

In the root of your blog directory, a config.yml is created to configure your blog in a global use.

A example of the config.yml::

    # All of them are required
    title: My blog
    subtitle: A blog powered by hazel
    domain: blog.example.com
    author: Myself
    email: me@example.com
    template: hazel

Template Configuration
----------------------

To personalize your blog style, template configuration is easily handled.

Example::

    # All of them are optional
    index_post: 3
    date_format: '%B %d, %Y'
    analytics:
    twitter:

Rather than the restrict standard of the general config file, template configuration is more flexible and you can define your own configurations for global use.
