# conf.py

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Project information
project = 'HOPYBOX'
author = 'HOStudio123'
release = '1.9.8'

# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = []

# Options for HTML output
html_theme = 'pyramid'

html_static_path = ['_static']

# Custom CSS
def setup(app):
    app.add_css_file('custom.css')
