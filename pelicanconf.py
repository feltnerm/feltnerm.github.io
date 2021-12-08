#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mark Feltner'
SITENAME = "Mark Feltner's Website"
SITENAME_SHORT = "Mark Feltner's Website"
EMAIL = 'mark@feltner.me'
SITEURL = ''
DESCRIPTION = "The thoughts and writings of Mark James Feltner."

THEME = 'theme/feltnerm'
DEVELOP = True

PATH = 'content'

TIMEZONE = 'America/Chicago'
READERS = {
    'html': None
}

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = [
    'static/CNAME',
    'static/robots.txt',
    'static/hackers.txt',
    'static/humans.txt'
]

EXTRA_PATH_METADATA = {
    'static/CNAME': { 'path': 'CNAME' },
    'static/robots.txt': { 'path': 'robots.txt' },
    'static/hackers.txt': { 'path': 'hackers.txt' },
    'static/humans.txt': { 'path': 'humans.txt' }
}

REPO_HOME = 'https://github.com/feltnerm/blog'

TWITTER_USERNAME = 'feltnermj'
GITHUB_USERNAME = 'feltnerm'
LASTFM_USERNAME = 'plugitin'
FACEBOOK_USERNAME = 'feltnerm'

ANALYTICS = {
    'GOOGLE': ''
}

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DIRECT_TEMPLATES = ['index', 'archives', 'tags']

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}.html'
INDEX_SAVE_AS = 'blog/index.html'
ARCHIVES_URL = 'blog/archive'
ARCHIVES_SAVE_AS = 'blog/archive/index.html'
YEAR_ARCHIVE_URL = 'blog/{date:%Y}/'
YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCHIVE_URL = 'blog/{date:%Y}/{date:%m}'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/'
DAY_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/index.html'
TAG_URL = 'blog/tag/{slug}/'
TAG_SAVE_AS = 'blog/tag/{slug}/index.html'
TAGS_URL = 'blog/tags/'
TAGS_SAVE_AS = 'blog/tags/index.html'

# don't generate these:
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''

MARKDOWN = {
    'extension_configs': {
        # 'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.smarty': {},
        'markdown.extensions.sane_lists': {},

        # "proxy" for `markdown.extensions.extra``
        'pymdownx.extra': {},

        # emphasis that is more like GFM
        'pymdownx.betterem': {},

        # use emoji shortcodes
        'pymdownx.emoji': {},

        # code highlighting
        'pymdownx.highlight': {},
        'pymdownx.inlinehilite': {},
        'pymdownx.superfences': {},

        # turn markdown links into ... links
        'pymdownx.magiclink': {},

        # strict parsing of headers
        'pymdownx.saneheaders': {},

        # fancy symbols
        'pymdownx.smartsymbols': {},


        # @todo: where did this extension go?!
        # 'markdown.extensions.headerid': {},
    },
    'output_format': 'html5',
}
