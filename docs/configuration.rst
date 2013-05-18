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
    #rsync
    host: 12.345.678.999
    user: username
    dest: /path/blog

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

Nginx Configuration
-------------------

Since hazel is a static blog generator, you don't need a web framework like tornado or flask. With a little configuration of nginx, your blog site will be extremely fastened::

    server {
        listen 80;
        server_name blog.example.com;

        root /path/to/site;
        index index.html;

        access_log /path/to/logs/access.log;
        error_log /path/to/logs/error.log;

        if ( $request_uri ~ "/index.html" ) {
            rewrite ^ /$1 permanent;
        }

        location / {
            try_files $uri.html $uri $uri/ =404;
        }
    }

BTW, don't forget to create the 'logs' directory!
