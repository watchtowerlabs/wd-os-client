# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os
import time

os.chdir('..')
import versioneer

__version__ = versioneer.get_versions()['version']

del versioneer
os.chdir('docs')

# -- Project information -----------------------------------------------------

project = 'SatNOGS Client'
copyright = '2016-{}, Libre Space Foundation'.format(time.strftime('%Y'))
author = 'SatNOGS'
version = __version__
release = __version__

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']
autodoc_mock_imports = [
    'Hamlib',
    'gps',
    'h5py',
    'numpy',
    'matplotlib',
]
autodoc_default_options = {'members': True, 'private-members': True, 'undoc-members': True}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_context = {
    "display_gitlab": True,
    "gitlab_user": "librespacefoundation",
    "gitlab_repo": "satnogs/satnogs-client",
    "gitlab_version": "master",
    "conf_py_path": "/docs/",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
