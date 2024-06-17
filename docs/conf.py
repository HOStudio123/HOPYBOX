# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('.'))
project = 'HOPYBOX'
copyright = '2022~2024'
author = 'HOStudio123'
release = '1.8.0'
extensions = [
    'sphinx.ext.autodoc', 
    'sphinx.ext.napoleon',  
    'sphinx.ext.viewcode', 
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_options = {
}

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
}


intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

napoleon_google_docstring = True
napoleon_numpy_docstring = False

def setup(app):
    pass
