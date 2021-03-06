#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "I-Kang Ding"
SITENAME = "I-Kang's Notes"
THEME = "pelican-themes/pelican-bootstrap3"
PYGMENTS_STYLE = "default"

# Use this for local development
# pelican content
SITEURL = "."
RELATIVE_URLS = True

# Use this for publishing
# pelican content -o ../ikding.github.io/ -s pelicanconf.py
# SITEURL = "https://ikding.github.io"
# RELATIVE_URLS = False

PATH = "content"

TIMEZONE = "US/Pacific"
DEFAULT_DATE_FORMAT = "%Y-%m-%d (%a)"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
MENUITEMS = [
    ("About Me", "/pages/about-me.html"),
    ("Resume", "/resume/"),
    ("Career Development", "/tag/career.html"),
    ("Data Science", "/tag/data_science.html"),
    ("Climate Tech", "/tag/climate_tech.html"),
    ("Misc", "/tag/misc.html"),
    ("Archives", "/archives.html"),
]

# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ("GitHub", "https://github.com/ikding"),
    ("Twitter", "https://twitter.com/ikding"),
    ("LinkedIn", "https://www.linkedin.com/in/ikding"),
)

# Add year archives
YEAR_ARCHIVE_SAVE_AS = "posts/{date:%Y}/index.html"

DEFAULT_PAGINATION = 10

JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.i18n"],
}
PLUGIN_PATHS = ["pelican-plugins/"]
PLUGINS = ["i18n_subsites", "readtime", "embed_tweet"]

# pelican-bootstrap3 custom options
# CUSTOM_CSS = 'static/custom.css'

GITHUB_USER = "ikding"
GITHUB_REPO_COUNT = 3
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True
BOOTSTRAP_THEME = "yeti"

USE_FOLDER_AS_CATEGORY = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_ARTICLE_INFO_ON_INDEX = True

# This can be used to add favicon, which I'm not currently using
# https://stackoverflow.com/questions/31270373/how-to-add-a-favicon-to-a-pelican-blog
# STATIC_PATHS = ["extra/favicon.ico"]
# EXTRA_PATH_METADATA = {"extra/favicon.ico": {"path": "favicon.ico"}}

SHOW_ABOUTME = True
AVATAR = "/images/profile.jpg"
ABOUT_ME = """
Doing data mining on mining data at KoBold Metals.
Stanford Engineering Ph.D.
<br/>
<br/>
Interested in intersection of machine learning, data science, and climate change.
"""

DISQUS_SITENAME = "ikding"
GOOGLE_ANALYTICS = "UA-19568221-4"
