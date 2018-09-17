#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'John Gage'
SITENAME = 'CalWaterDay new'
SITESUBTITLE = 'California Water 641'

SITEURL = 'http://johngage.github.io'

# Time and Date settings
TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

THEME = 'themes/pelican-bootstrap3'

#Paths
PATH = 'content'
# PATH settings
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']

STATIC_PATHS = ['images', 'data', 'publications']

OUTPUT_PATH = 'output/'

#PLUGIN_PATHS = ['./pelican-plugins', './plugins']

#PLUGINS = ['render_math', 'ipynb.markup', 'better_codeblock_line_numbering']


SIDEBAR_NAME = AUTHOR
SIDEBAR_EMAIL = "john.gage@gmail.com"
SIDEBAR_TAGS = ['CalWaterDay',
                'Califoria Schools',
                'Jupyter Notebooks for Schools',
                'JupyterForNews',
                'Water Data',
                ]
#DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
#RECENT_POST_COUNT = 3


MENUITEMS = [('Home', '/'),
             ('Books', '/pages/books/'),
             ('About', '/pages/about/'),
             ('Links', '/pages/links/'),
             ]



#Basic settings
DEFAULT_CATEGORY = 'misc'
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
IGNORE_FILES = ['.#*', '.ipynb_checkpoints']
MARKDOWN = {}


# Extention
MARKUP = ('md', 'ipynb')

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
#MD_EXTENSIONS = [
#    'codehilite(css_class=highlight,linenums=False)',
#    'extra'
#    ]


# URL settings
ARTICLE_URL = 'articles/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'



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

PLUGIN_PATHS = ['pelican-plugins','plugins' ]
#PLUGINS = ['i18n_subsites', ]
PLUGINS = [
    'i18n_subsites','series','tag_cloud',
    'liquid_tags.img', 'liquid_tags.video', 'liquid_tags.youtube', #'liquid_tags.notebook',
    'liquid_tags.vimeo',
    'liquid_tags.include_code',
    #'pelican_javascript',
    'related_posts',
    'render_math','tipue_search',
    #'pelican-ipynb.markup',
    'neighbors',
    #'bootswatch_markdown_css',
    ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
