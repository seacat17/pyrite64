# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Pyrite64'
copyright = '2026, Max Bebök'
author = 'Max Bebök'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import subprocess

extensions = ['myst_parser', 'breathe']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv']

# -- C++ API docs (Doxygen XML -> Breathe) -----------------------------------
# Doxygen is run automatically here as a silent XML backend; it never produces
# its own site. Breathe then renders that XML inside this Sphinx build.
_docs_dir = os.path.abspath(os.path.dirname(__file__))
_doxygen_xml = os.path.join(_docs_dir, "_build", "doxygen", "xml")

os.makedirs(_doxygen_xml, exist_ok=True)

# Run on every build so the API docs always match the headers. Skip if the
# doxygen binary is missing (e.g. minimal env) but XML already exists.
try:
    subprocess.run(["doxygen", "Doxyfile"], cwd=_docs_dir, check=True)
except (FileNotFoundError, subprocess.CalledProcessError) as err:
    if not os.path.isdir(_doxygen_xml):
        raise
    print(f"[conf.py] WARNING: doxygen not run ({err}); using existing XML.")

breathe_projects = {"pyrite64": _doxygen_xml}
breathe_default_project = "pyrite64"
breathe_default_members = ("members",)


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# https://alabaster.readthedocs.io/en/latest/customization.html
html_theme = 'furo'
html_static_path = ['_static']
html_favicon = '_static/favicon.ico'

html_css_files = [
    'custom.css',
]

html_theme_options = {
  "sidebar_hide_name": True,    
  "light_logo": 'logo.png',
  "dark_logo": 'logo.png',
  
  "light_css_variables": {
    "font-stack": "Noto, Arial, sans-serif",
  },
} 
