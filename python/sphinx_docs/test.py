#! /usr/bin/env python3

import re

# Simulated content based on your description
content = '''
static constexpr char PyBlackOilSimulator_filename_constructor_docstring[] =
    "Constructor using a deck file name.\\n\\n"
    ":param deck_filename: The file name of the deck to be used for the simulation.";
'''

# Updated regex pattern
#pattern = re.compile(r'static constexpr char (\w+)\[\] =\s*"\n\s*([^"]*"(?:\n\s*"[^"]*")*);', re.DOTALL)
#pattern = re.compile(r'static constexpr char (\w+)\[\] =\s*"\n\s*', re.DOTALL)
# Adjusted regex pattern
#pattern = re.compile(
#    r'static constexpr char (\w+)\[\] =\n\s*"((?:[^"\\]|\\.|"(?=\n))+)"\s*;',
#    r'static constexpr char (\w+)\[\] =\n\s*"((?:[^"\\]|\\.|"(?=\n))+)"\s*;',
#    re.DOTALL
#)
# Regex pattern for matching C++ raw string literals
pattern = re.compile(
    r'static constexpr char (\w+)\[\] = R"\((.*?)\)"\s*;',
    re.DOTALL
)

matches = pattern.findall(content)
for match in matches:
    print(match)
