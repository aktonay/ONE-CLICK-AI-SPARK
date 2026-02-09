# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
project = 'One Click AI Spark'
copyright = '2026, Mohammad Asif Khan'
author = 'Mohammad Asif Khan'
release = '3.0.2'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'myst_parser',
]

# MyST configuration — enable heading anchors so in-page TOC links work
myst_heading_anchors = 3
suppress_warnings = ['myst.xref_missing']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'

# Static assets
html_static_path = ['_static']
html_css_files = ['custom.css']
html_js_files = ['custom.js']

html_logo = None
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False,
}

# Project links shown in the sidebar
html_context = {
    'display_github': True,
    'github_user': 'aktonay',
    'github_repo': 'ONE-CLICK-AI',
    'github_version': 'main',
    'conf_py_path': '/docs/',
}
