#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'John Gage'
SITENAME = 'Water, Power, Network'
SITESUBTITLE = 'City Critical Infrastructure'
SITEURL = ''
#SITEURL = 'http://johngage.github.io/water'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# PATH settings
PATH = 'content'
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']

STATIC_PATHS = ['images',
                'data',
                'publications',
                'extra'
                ]

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'

#THEME settings

THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#EXTRA_HEADER = open('_nb_header.html').read()#.decode('utf-8')
#this reads in the huge file of css definitions: where did this come from?
FAVICON = 'images/sunlight.png'

CUSTOM_CSS = 'static/css/custom.css'
CUSTOM_JS = 'static/js/custom.js'
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
    'extra/custom.js': {'path': 'static/js/custom.js'}
}
# for Tique Search Plugin
DIRECT_TEMPLATES = ('index','tags', 'categories', 'authors', 'archives', 'search')

#Basic settings
USE_FOLDER_AS_CATEGORY = False

DEFAULT_CATEGORY = 'misc'
#Top menus
DISPLAY_CATEGORIES_ON_MENU = False

DISPLAY_PAGES_ON_MENU = True
#Note all urls are relative to output folder, not content
MENUITEMS = [
             #('About', '/pages/about'),
             ('Posts', '/posts/2018'),
             #('Tags', '/tags'),
             ('Categories', '/categories.html')
             ]

#Sidebar Elements
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
RECENT_POST_COUNT = 4

DISPLAY_CATEGORIES_ON_SIDEBAR = True

DISPLAY_SERIES_ON_SIDEBAR = True

SIDEBAR_IMAGES_HEADER = 'My Images'
SIDEBAR_IMAGES = ["/images/sunlight.png" ]

DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
SERIES_TEXT = 'Article %(index)s of the %(name)s series'
#sidebar options
   # Tag Cloud Options
DISPLAY_SERIES_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
TAG_CLOUD_MAX_ITEMS = 10
   # Recent Posts in Sidebas
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
RECENT_POST_COUNT = 3
   # Series infor on sidebar
SHOW_SERIES = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True

ARCHIVES_SAVE_AS = 'archives.html'
DISPLAY_ARCHIVE_ON_MENU = True
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'


IGNORE_FILES = ['.#*', '.ipynb_checkpoints']

I18N_TEMPLATES_LANG = 'en'
MARKUP = ('md', 'ipynb', 'html')
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.toc': {'title': 'Table of contents:'}, #consider out
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
	    'markdown.extensions.tables': {},
        'markdown.extensions.admonition': {},
        'pymdownx.smartsymbols': {},
    },
    'output_format': 'html5',
}

# Blogroll
LINKS = (
        ('Pelican', 'http://getpelican.com/'),
        ('Python.org', 'http://python.org/'),
        ('Jinja2', 'http://jinja.pocoo.org/'),
        ('Learn Enough to be dangerous', 'https://www.learnenough.com/dev-environment-tutorial#sec-native_os_setup'),
        ('Full Stack Python', 'https://www.fullstackpython.com/'),
        ('How I Built This Site','https://pythonforundergradengineers.com/how-i-built-this-site-1.html')
        )

# Social widget
SOCIAL = (
         ('Berkeley', 'http://berkeley.edu'),
         ('Berkeley Institute of Data Sciences', 'http://berkeley.edu'),
          ('Time', 'http://timeanddate.com'))

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['pelican-plugins' ]
#PLUGINS = ['i18n_subsites', ]
PLUGINS = [
    'i18n_subsites','series','tag_cloud',
    'liquid_tags.img', 'liquid_tags.video', 'liquid_tags.youtube', 'liquid_tags.notebook',
    'liquid_tags.vimeo',
    'liquid_tags.include_code',
    #'pelican_javascript',
    'related_posts',
    'render_math','tipue_search',
    'pelican-ipynb.markup',
    'neighbors',
    #'bootswatch_markdown_css',
    #'ipynb.markup',
    'better_codeblock_line_numbering'
    ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
I18N_TEMPLATES_LANG = 'en'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# URL settings
#ARTICLE_URL = 'articles/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
#ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
#PAGE_URL = 'pages/{slug}/'
#PAGE_SAVE_AS = 'pages/{slug}/index.html'
