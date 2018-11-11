#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from pyembed.rst import PyEmbedRst
PyEmbedRst().register()


AUTHOR = u'Jose Dias'
SITENAME = u'Jose Dias'
SITEURL = ''

#MARKUP = ('md','ipynb')
PATH = 'content'

#THEME = "/home/josedias/projects/pelican-themes/pelican-octopress-theme-master"
THEME = "/home/josedias/projects/pelican-themes/waterspill-en"
PLUGIN_PATHS = ['/home/josedias/projects/pelican-plugins']
PLUGINS = ['render_math','liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook']


MATH_JAX = {'tex_extensions': ['color.js','mhchem.js'], 'latex_preview':['Tex']}



TIMEZONE = 'America/Sao_Paulo'

#DATE_FORMATS = { u'en': '%a, %d %b %Y',}

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
         ('GitHub', 'https://github.com'),)

# Social widget
SOCIAL = (('500px', 'https://500px.com/jdiasn'),
	  ('Facebook','https://www.facebook.com/jose.dias.756')
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
