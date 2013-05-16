Getting Started
===============

Installation
------------

Install hazel uisng pip::

    pip install hazel

Git::

    git clone https://github.com/shunfan/hazel.git
    cd hazel
    python setup.py install

Initiation
----------

Target a directory::

    cd path_to_an_empty_directory

Start to initiate your blog::

    hazel init

All basic directories will be created and the default template 'hazel' will be installed.

Write a post
------------

Write a post file using terminal::

    hazel write post_title

Then, a markdown file will be created in the posts directory.

Generation
----------

After writing, let's generate the blog::

    hazel generate

Overall, the blog has been built. What you gonna do next is :ref:`configuration`.
