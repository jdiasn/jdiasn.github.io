#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
from pyembed.rst import PyEmbedRst
PyEmbedRst().register()


AUTHOR = u'Jose Dias'
SITENAME = u'Jose Dias'
SITEURL = ''

PATH = 'content'

#THEME = "/home/josedias/projects/pelican-themes/pelican-octopress-theme-master"
#home = os.environ['HOME']
#THEME = "{0}/projects/pelican-themes/waterspill-en".format(home)
#PLUGIN_PATHS = ["{0}/projects/pelican-plugins".format(home)]
THEME = os.environ['THEME_PEL']
PLUGIN_PATHS = os.environ['PLUGIN_PATHS_PEL']
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

# Social widget
SOCIAL = (('ResearchGate', 'https://www.researchgate.net/profile/Jose_Neto111'),
          ('ORCID','https://orcid.org/0000-0002-8488-8486'),
          ('500px', 'https://500px.com/jdiasn'),
	  ('Facebook','https://www.facebook.com/jose.dias.756')
          )

# Blogroll
LINKS = (#('Pelican', 'http://getpelican.com/'),
         #('Python.org', 'http://python.org/'),
         #('Jinja2', 'http://jinja.pocoo.org/'),
         ('GitHub', 'https://github.com'),
         ('Data Browser', 'http://gop.meteo.uni-koeln.de/~hatpro/dataBrowser/dataBrowser1.html'),
         ('Working Folders','http://gop.meteo.uni-koeln.de/~jdias/folders/'),
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
