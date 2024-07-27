import os
import sys
from sphinx.application import Sphinx

# -- Path setup --------------------------------------------------------------

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'HOPYBOX'
author = 'HOStudio123'
release = '1.9.8'

# -- General configuration ---------------------------------------------------

# Extensions for Sphinx documentation
extensions = [
    'sphinx.ext.autodoc',  # Auto-generate API documentation
    'sphinx.ext.napoleon', # Support for NumPy and Google style docstrings
    'sphinx.ext.viewcode', # Add links to the source code
    'sphinx_rtd_theme',    # ReadTheDocs theme for Sphinx
]

# Path to the templates and static files
templates_path = ['_templates']
html_static_path = ['_static']

# Patterns to ignore when looking for source files
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# HTML theme and options
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'canonical_url': '',  # URL for canonical links
    'analytics_id': '',   # Google Analytics ID
    'logo_only': True,
    'display_version': True,
}

# Custom CSS and JavaScript
def setup(app: Sphinx) -> None:
    app.add_css_file('custom.css')  # Add custom CSS file
    # Uncomment the following line to add custom JavaScript file
    # app.add_js_file('custom.js')
