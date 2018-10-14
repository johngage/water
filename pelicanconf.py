#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'John Gage'
SITENAME = 'CalWaterDay 6'
SITESUBTITLE = 'California Water Data Initiative'

SITEURL = '' #'http://johngage.github.io'

# Time and Date settings
TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

#THEME settings

THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'
PLUGIN_PATHS = ['/pelican-plugins', '/plugins']

PLUGINS = ['render_math', 'ipynb.markup', 'better_codeblock_line_numbering']

# PATH settings
PATH = 'content'
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']

STATIC_PATHS = ['images',
                'data',
                'publications'
                ]

#OUTPUT_PATH = 'output/'

# for Tique Search Plugin
DIRECT_TEMPLATES = ('index','tags', 'categories', 'authors', 'archives', 'search')

SIDEBAR_NAME = AUTHOR
SIDEBAR_EMAIL = "john.gage@gmail.com"
SIDEBAR_TAGS = ['CalWaterDay',
                'Califoria Schools',
                'Jupyter Notebooks for Schools',
                'Pelican',
                'Data Science',
                'water',
                ]
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
RECENT_POST_COUNT = 3

MENUITEMS = [('Pages1', '/pages/Great Books'),
             ('Posts2', '/posts/2018'),
             ('Tags', '/tags'),
             ('Author', 'authors.html')
             ]

DISPLAY_SERIES_ON_SIDEBAR = True

#Basic settings
USE_FOLDER_AS_CATEGORY = False

DEFAULT_CATEGORY = 'misc'
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
IGNORE_FILES = ['.#*', '.ipynb_checkpoints']
#MARKDOWN = {}
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True


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
ARCHIVES_SAVE_AS = 'archives.html'
DISPLAY_ARCHIVE_ON_MENU = True
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'


DEFAULT_DATE_FORMATS = '%a, %m/%d/%Y'
# LOCALE = ('en_US')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
        ('Pelican', 'http://getpelican.com/'),
        ('Python.org', 'http://python.org/'),
        ('Jinja2', 'http://jinja.pocoo.org/'),
        ('Enough to be dangerous', 'https://www.learnenough.com/dev-environment-tutorial#sec-native_os_setup'),
        )

# Social widget
SOCIAL = (('Berkeley', 'http://berkeley.edu'),
          ('Berkeley Institute of Data Sciences', 'http://berkeley.edu'),)

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
