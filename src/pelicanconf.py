#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Roman Saldygashev'
SITENAME = "Roman Saldygashev's homepage"
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'output'

TIMEZONE = 'Asia/Yekaterinburg'

DEFAULT_LANG = 'en'

LOCALE = ('en_US.utf8', 'ru_RU.utf8')

DATE_FORMATS = {
    'en': ('en_US.utf8', '%Y %b %d'),
    'ru': ('ru_RU.utf8', '%d %B %Y')
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('PhyShader for Mantra', 'https://github.com/groundflyer/physhader-for-mantra'),)

# Social widget
SOCIAL = (('vimeo', 'https://vimeo.com/user2461269'),
          ('github', 'https://github.com/groundflyer'),
          ('envelope', 'mailto:sldg.roman@gmail.com'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

TYPOGRIFY = True

DISPLAY_PAGES_ON_MENU = True
STATIC_PATHS = ('images', 'misc')

THEME = "../../pelican-themes/Flex"

# Flex config
SITETITLE = "Roman Saldygashev"
SITESUBTITLE = "Graphonium miner"
SITELOGO = '/images/logo.jpg'
SITEDESCRIPTION = "CG R&D blog"
# BROWSER_COLOR = '#4285f4'
COPYRIGHT_YEAR = 2016
MAIN_MENU = True
CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}
ROBOTS = 'index, follow'
# PYGMENTS_STYLE = 'emacs'
MENUITEMS= (('По-русски', '/ru'),)


# plugins
ppp='../../pelican-plugins'
PLUGIN_PATHS = [ppp, ppp+'/pelican-gist', ppp+'/pelican_vimeo']
PLUGINS = ['i18n_subsites', 'render_math', 'pelican-cite', 'pelican_gist', 'pelican_vimeo']
JINJA_EXTENSIONS = ['jinja2.ext.i18n']

# i18n
I18N_SUBSITES = {
    'en': {
        'SITENAME': SITENAME,
        'SITESUBTITLE': SITESUBTITLE,
        'STATIC_PATHS': STATIC_PATHS,
        'THEME': THEME,
        'MENUITEMS': MENUITEMS
    },
    'ru': {
        'SITENAME': 'Домашняя страница Салдыгашева Романа',
        'SITETITLE': 'Роман Салдыгашев',
        'SITESUBTITLE': 'Добываю графоний',
        'STATIC_PATHS': STATIC_PATHS,
        'THEME': THEME,
        'MENUITEMS': (('English', '/en'),)
    }
}

# pelican-cite
PUBLICATIONS_SRC = 'content/misc/pubs.bib'
