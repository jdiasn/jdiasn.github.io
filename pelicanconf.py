#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from pyembed.rst import PyEmbedRst
PyEmbedRst().register()


AUTHOR = u'Jose Dias'
SITENAME = u'Jose Dias'
SITEURL = ''

PATH = 'content'

THEME = "/home/josedias/projects/pelican-themes/waterspill-en"
PLUGIN_PATHS = ['/home/josedias/projects/pelican-plugins']
PLUGINS = ["render_math"]


MATH_JAX = {'tex_extensions': ['color.js','mhchem.js'], 'latex_preview':['Tex']}



TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'en'

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
