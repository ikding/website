Pelican Readtime Plugin
#######################

:date: 2020-04-18
:tags: data_science
:slug: pelican-readtime-plugin
:authors: I-Kang Ding
:summary: How to add readtime plugin in pelican


In the beginning of 2020, I started a goal of writing more professionally. I did not like the idea of putting my blog articles in pay-wall sites such as medium, so I decided to use my own static site generator and host my blog in GitHub pages.

In picking a `static site generator <https://www.fullstackpython.com/static-site-generator.html>`_, I have poked around at a few libraries out there, and landed on `Pelican <https://blog.getpelican.com>`__. This, in retrospect, was an obvious choice because among the Python static generators (`pelican <https://blog.getpelican.com>`__, `lektor <https://github.com/lektor/lektor>`_, `nikola <https://github.com/getnikola/nikola>`_), pelican has been around for a long time, and has an extensive `plugin <https://github.com/getpelican/pelican-plugins>`_ system.

The plugin I want to talk in this post is the `readtime <https://github.com/getpelican/pelican-plugins/tree/master/readtime>`_ plugin. From the plugin's own site:

    An article estimated read time plugin for Pelican static site generator. After Pelican generated the content of each page, the plugin read through the generated HTML content and strip all the tags, count all the word, then utilize average human read speed to calculate the read time of each article. The read time is passed over to the 'content' object of the article so Jinja template can use it to display the read time on wherever appropriate.

It's a short and sweet plugin, but it took some time to make it work with my site. So I figured that I'll writeup what worked for me, in case it helps others in the future.

First, I have added plugin name to the ``pelicanconf.py`` file:

.. code-block:: python

   PLUGINS=[ ... , 'pelican-readtime']

Then, you can put the following code in whichever template you want. I was using `pelican-bootstrap3 <https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3>`_ template, so I put the following `code block <https://github.com/ikding/website/blob/ac1713ac475f3c927f54ac3da339ac1819623d22/pelican-themes/pelican-bootstrap3/templates/includes/article_info.html#L6-L10>`__ in my ``article_info.html``:

.. code-block:: html

    {% if article.readtime %}
        <span class="label label-default">Read time</span>
        <span class="published">
            <i class="fa fa-hourglass"></i> {{article.readtime.minutes}} min.</span>
    {% endif %}

I also added the following `code block <https://github.com/ikding/website/blob/ac1713ac475f3c927f54ac3da339ac1819623d22/pelican-themes/pelican-bootstrap3/templates/archives.html#L20-L22>`__ to ``archives.html``:

.. code-block:: html

    {% if article.readtime %}
        <span class="categories-timestamp">({{article.readtime.minutes}} min read)</span>
    {% endif %}

And that's all there is to it! After you had the readtime properly configured, you will be able to see the read time of your articles in the article page:

.. image:: https://user-images.githubusercontent.com/7269845/79665216-60072000-8183-11ea-8d3f-c08577d095f9.png
    :align: center
    :alt: readtime-article-page
    :width: 600 px

... as well as the archive page:

.. image:: https://user-images.githubusercontent.com/7269845/79665208-5f6e8980-8183-11ea-834b-bdc30dad4048.png
    :align: center
    :alt: readtime-article-page
    :width: 800 px
