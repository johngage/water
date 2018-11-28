#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.
print ("Made it here 1")

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *
print ("Made it here 2")
# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://johngage.github.io/water'
RELATIVE_URLS = True
print ("Made it here 3")

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
print ("Made it here 4")

DELETE_OUTPUT_DIRECTORY = True
print ("Made it here 5")


# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
