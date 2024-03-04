# docs/pybind_docstrings.py
import json
from docutils import nodes
from docutils.parsers.rst import Directive

class PybindDocstringsDirective(Directive):
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}

    def run(self):
        env = self.state.document.settings.env
        docstrings_path = env.app.config.pybind_docstrings_path
        with open(docstrings_path, 'r') as file:
            docstrings = json.load(file)
        
        result = []
        for func_name, docstring in docstrings.items():
            para = nodes.paragraph()
            para += nodes.strong(text=f"{func_name}()")
            para += nodes.paragraph(text=docstring)
            result.append(para)
        
        return result

def setup(app):
    app.add_config_value('pybind_docstrings_path', None, 'env')
    app.add_directive("pybind_docstrings", PybindDocstringsDirective)
