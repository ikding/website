#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'I-Kang Ding'
SITENAME = "I-Kang Ding's site"
SITEURL = '.'
THEME = '/Users/ikding/Documents/data_science/projects/pelican-themes/pelican-bootstrap3'

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# MENUITEMS = [
#     ("Just Programming Posts", "/category/programming.html"),
#     ("Coder's Guide", "/codersguide/"),
#     ("Notebooks", "https://nbviewer.jupyter.org/github/toumorokoshi/notebooks/tree/master/"),
# ]
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('GitHub', 'https://github.com/ikding'),
    ('Twitter', 'https://twitter.com/ikding'),
    ('LinkedIn', 'https://www.linkedin.com/in/ikding')
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
PLUGIN_PATHS = ['/Users/ikding/Documents/data_science/projects/pelican-plugins/']
PLUGINS = ['i18n_subsites']

# pelican-bootstrap3 custom options
# CUSTOM_CSS = 'static/custom.css'

GITHUB_USER = 'ikding'
GITHUB_REPO_COUNT = 3
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True
BOOTSTRAP_THEME = 'yeti'

USE_FOLDER_AS_CATEGORY = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True

SHOW_ABOUTME = True
AVATAR = "/images/profile.jpg"
ABOUT_ME = """
Data Science Manager at Capital One, focused on anti-fraud ML models.
Stanford Engineering Ph.D.
<br/>
<br/>
Interested in data science, renewable energy, and climate change.
"""
