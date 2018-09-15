#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'John Gage'
SITENAME = 'CalWaterDay'
SITESUBTITLE = 'California Water Hackathon'

SITEURL = 'http://johngage.github.io'
SIDEBAR_NAME = AUTHOR
SIDEBAR_EMAIL = "john.gage@gmail.com"
SIDEBAR_TAGS = ['CalWaterDay',
                'NetDay',
                'WaterCurriculum',
                'JupyterForNews',
                ]
MENUITEMS = [('Home', '/'),
             ('Books', '/pages/books/'),
             ('About', '/pages/about/'),
             ('Links', '/pages/links/'),
             ]
SITEURL = ''

SITEURL = 'http://jjakimoto.github.io'
SIDEBAR_NAME = AUTHOR
SIDEBAR_EMAIL = "f.j.akimoto@gmail.com"
SIDEBAR_TAGS = ['Machine Learning',
                'Deep Learning',
                'Finance',
                'Python',
                ]
MENUITEMS = [('Home', '/'),
             ('Books', '/pages/books/'),
             ('About', '/pages/about/'),
             ('Links', '/pages/links/'),
             ]

PATH = 'content'


DEFAULT_LANG = 'en'

 Basic settings
DEFAULT_CATEGORY = 'misc'
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
IGNORE_FILES = ['.#*', '.ipynb_checkpoints']
MARKDOWN = {}

# PATH settings
OUTPUT_PATH = 'output/'
PATH = 'content'
STATIC_PATHS = ['images', 'data', 'publications']
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']

# Extention
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./pelican-plugins', './plugins']
PLUGINS = ['render_math', 'ipynb.markup', 'better_codeblock_line_numbering']

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
MD_EXTENSIONS = [
    'codehilite(css_class=highlight,linenums=False)',
    'extra'
    ]


# URL settings
ARTICLE_URL = 'articles/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Time and Date settings
TIMEZONE = 'America/Los Angeles'

DEFAULT_DATE_FORMATS = '%a, %m/%d/%Y'
# LOCALE = ('en_US')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
