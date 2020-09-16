Pelican Embed-Tweet Plugin
##########################

:date: 2020-09-15
:tags: data_science
:slug: pelican-embed-tweet-plugin
:authors: I-Kang Ding

In this article, I wrote about how to use pelican ``embed_tweet`` plugin in Pelican static site generator, which is useful for embedding tweet into your own blog posts, like so: t#ikding/status/1306120884646674438

In the beginning of 2020, I started a goal of writing more professionally. I did not like the idea of putting my blog articles in pay-wall sites such as medium, so I decided to use my own static site generator and host my blog in GitHub pages.

The `static site generator <https://www.fullstackpython.com/static-site-generator.html>`_, I picked is `Pelican <https://blog.getpelican.com>`__. The pelican plugin I want to talk in this post is the `embed-tweet <https://github.com/lqez/pelican-embed-tweet>`_ plugin, which is useful for embedding tweet into your own blog posts. (If you're interested in how I landed on Pelican, I talked about that briefly over in `Pelican Readtime Plugin <{filename}../data_science/2020-04-18_pelican_readtime.rst>`_ article.)

It's a short and sweet plugin, but it took some time to make it work with my site. So I figured that I'll writeup what worked for me, in case it helps others in the future.

This particular plugin is not on PyPI, so what I did to get it to work on my system was to first copy the file content of `embed_tweet.py <https://github.com/lqez/pelican-embed-tweet/blob/master/embed_tweet.py>`_ into my own file system in the ``pelican-plugins`` subfolder. I also made a subfolder and ``__init__.py`` file, like so:

.. code-block:: sh

    $ tree pelican-plugins

    pelican-plugins
    └── embed_tweet
        ├── __init__.py
        └── embed_tweet.py

Then, I added plugin name to the ``pelicanconf.py`` file:

.. code-block:: python

    PLUGINS=[ ... , "embed_tweet"]

Then, in the main body of my article, I can just highlight the tweet using the ``t#`` prefix. (Please remove one of the extra ``#`` from the line below.)

.. code-block:: rst

    This article is from t##ikding

    And here is one of his tweets: t##ikding/status/1306120884646674438

    By the way, the suffix is ``t#``, not ``t##``. I added the extra ``#`` to stop embed-tweet from rendering the tweet.

The embed-tweet plugin will automatically convert it to an embedded tweet:

.. code-block:: rst

    This article is from t#ikding

    And here is one of his tweets: t#ikding/status/1306120884646674438
