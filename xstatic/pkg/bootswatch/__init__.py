
"""
XStatic resource package

See package 'XStatic' for documentation and basic tools.
"""

# official name, upper/lowercase allowed, no spaces
DISPLAY_NAME = 'bootswatch'

# name used for PyPi
PACKAGE_NAME = 'XStatic-%s' % DISPLAY_NAME

NAME = __name__.split('.')[-1] # package name (e.g. 'foo' or 'foo_bar')
                               # please use a all-lowercase valid python
                               # package name

VERSION = '3.3.7' # version of the packaged files, please use the upstream
                  # version number
BUILD = '0' # our package build number, so we can release new builds
             # with fixes for xstatic stuff.
PACKAGE_VERSION = VERSION + '.' + BUILD # version used for PyPi

DESCRIPTION = "%s %s (XStatic packaging standard)" % (DISPLAY_NAME, VERSION)

PLATFORMS = 'any'
CLASSIFIERS = []
KEYWORDS = 'bootswatch xstatic'

# XStatic-* package maintainer:
MAINTAINER = 'Rob Cresswell'
MAINTAINER_EMAIL = 'robert.cresswell@outlook.com'

# this refers to the project homepage of the stuff we packaged:
HOMEPAGE = 'http://bootswatch.com'

# this refers to all files:
LICENSE = 'MIT'

from os.path import join, dirname
BASE_DIR = join(dirname(__file__), 'data')
# linux package maintainers just can point to their file locations like this:
#BASE_DIR = '/usr/share/javascript/' + NAME

# location of the Javascript file that's the entry point for this package, if
# one exists, relative to BASE_DIR


LOCATIONS = {
    # CDN locations (if no public CDN exists, use an empty dict)
    # if value is a string, it is a base location, just append relative
    # path/filename. if value is a dict, do another lookup using the
    # relative path/filename you want.
    # your relative path/filenames should usually be without version
    # information, because either the base dir/url is exactly for this
    # version or the mapping will care for accessing this version.
}
