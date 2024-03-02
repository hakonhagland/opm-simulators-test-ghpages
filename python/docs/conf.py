# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "opm-simulators"
copyright = "2024 Equinor ASA"
author = "Håkon Hægland"
release = "0.1"

# -- General configuration ---------------------------------------------------
import os
import sys

# For regular Python packages, the path to the package is usually added to sys.path
# here such that autodoc can find the modules. However, our Python module
#  opm.simulators.BlackOilSimulator is not generated yet. Since it is a pybind11
# extension module, it needs to be compiled as part of the opm-simulators build
# process (which requires building opm-common first and so on). The full compilation
# of opm-simulators requres both time and storage resources, so we do not want to
# do this as part of the documentation build. Instead, we will use a Python script
# to extract the doc strings from the C++ code.
#sys.path.insert(0, os.path.abspath("../opm"))
#extensions = ["sphinx.ext.autodoc", "sphinx_autodoc_typehints"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_context = {
    "display_github": True,
    "github_user": "OPM",
    "github_repo": "opm-simulators",
    "github_version": "master",
    "conf_py_path": "/python/docs/",
}
