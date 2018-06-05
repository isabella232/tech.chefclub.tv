#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHORS = (
    u'Rémy Hubscher',
    u'Gregory Tappero',
)
AUTHOR = "Tech @ ChefClub"

SITENAME = u'Tech @ ChefClub'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Social widget
SOCIAL = (('Github', 'https://github.com/ChefClub'),)

DEFAULT_PAGINATION = False

THEME = "pure"

COVER_IMG_URL = '/theme/sidebar.jpg'

SOCIAL = (
    ('envelope', 'https://www.chefclub.tv/'),
    ('rss', SITEURL + '/feeds/all.atom.xml'),
    ('github', 'https://github.com/ChefClub'),
)

MENUITEMS = (
    ('Archives', 'archives.html'),
    (u'À propos', 'pages/a-propos.html'),
)
STATIC_PATHS = ['images', 'documents', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

ARTICLE_URL = '{url}.html'
ARTICLE_SAVE_AS = '{url}.html'

PLUGIN_PATHS = ['plugins', '.']
PLUGINS = ['post_stats', 'better_figures_and_images', 'i18n_subsites']
I18N_SUBSITES = {'en': {}, 'fr': {}, }  # Override any default settings.
RESPONSIVE_IMAGES = True

DATE_FORMATS = {
    'en': ('en_US.UTF-8', '%a, %d %B %Y'),
    'fr': ('fr_FR.UTF-8', '%a %d %B %Y'),
}
