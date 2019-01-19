#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.
#print ("Made it here 1")

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *
#print ("Made it here 2")
# If your site is available via HTTPS, make sure SITEURL begins with https://
RELATIVE_URLS = False
SITEURL = 'https://johngage.github.io/water'

#print ("Made it here 3")
MENUITEMS = [
             #('About', '/pages/about'),
             ('2018 Posts', 'https://johngage.github.io/water/posts/2018'),
             ('2019 Posts', 'https://johngage.github.io/water/posts/2019'),
             ('Tags', 'https://johngage.github.io/water/tags.html'),
             ('MTags', 'tags.html'),
             ('JNotebook', 'https://johngage.github.io/water/tag/jupyter.html'),
             ('JNB', 'https://johngage.github.io/water/notebooks'),
             ]

#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
# RSS Feed Settings
FEED_DOMAIN = SITEURL
FEED_ATOM = None
FEED_RSS = 'rss'
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
RSS_FEED_SUMMARY_ONLY = True
#print ("Made it here 4")

DELETE_OUTPUT_DIRECTORY = True
#print ("Made it here 5")


# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
