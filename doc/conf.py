# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Links'
copyright = 'Katherine "Kati" Michel'
author = 'Katherine "Kati" Michel'
# release = '0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
# https://ablog.readthedocs.io/en/stable/
# https://ablog.readthedocs.io/en/stable/manual/markdown.html

extensions = [
    'myst_parser',
    'ablog',
    'sphinx.ext.intersphinx',
    'sphinxext.opengraph',
]
myst_update_mathjax = False

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# https://ablog.readthedocs.io/en/stable/manual/ablog-configuration-options.html
post_date_format = '%B %d, %Y'
post_auto_image = 0
post_show_prev_next = True
# skip_injecting_base_ablog_templates = True
# ablog_inject_templates_after_theme = True

# https://sphinxext-opengraph.readthedocs.io/en/latest/
# https://sphinxext-opengraph.readthedocs.io/en/latest/socialcards.html
# ogp_site_url = 'https://katherinemichel.github.io/'
# ogp_description_length = 300
# ogp_type = "article"
# ogp_use_first_image = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# html_sidebars = {
#     "blog": [
#         # ablog sidebars
#         'recentposts.html',  # This adds the recent posts sidebar
#         'tagcloud.html',
#         'categories.html',
#     ]
# }

html_sidebars = {
   # "blog": [
   "**": [
      # Comes from Alabaster theme
      # 'about.html',
      'searchfield.html',
      'navigation.html',
      'donation.html',
      # Ablog sidebars
      'postcard.html',
      'recentposts.html',
      'tagcloud.html',
      'categories.html',
      'archives.html',
      # 'authors.html',
      # 'languages.html',
      'locations.html',
    ]
}
