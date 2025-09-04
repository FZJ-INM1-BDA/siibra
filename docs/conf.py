import os
import sys

sys.path.insert(0, os.path.abspath("."))

project = "siibra"
html_title = "siibra - Software interface for interacting with brain atlases"

extensions = [
    "sphinx_design",
]

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_book_theme"

html_logo = "_static/siibra-logo-lightmode.png"
html_favicon = "_static/siibra_favicon.ico"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

html_theme_options = {
    "repository_url": "https://github.com/FZJ-INM1-BDA/siibra",
    "use_repository_button": False,
    "use_issues_button": False,
    "use_edit_page_button": False,
    "home_page_in_toc": False,
    "toc_title": "",
    "show_toc_level": 0,
    "collapse_navbar": False,
    "search_bar_text": "",
    "navbar_start": [],
    "navbar_center": [],
    "logo": {
        "image_light": "siibra-logo-lightmode.png",
        "image_dark": "siibra-logo-darkmode.png",
    },
    "extra_footer": "<div>This software code is funded from the European Union's Horizon 2020 Framework Programme for Research and Innovation under the Specific Grant Agreement No. 945539 (Human Brain Project SGA3).</div>",
    "use_fullscreen_button": False,
    "use_download_button": False,
}

html_sidebars = {
    "**": []
}
