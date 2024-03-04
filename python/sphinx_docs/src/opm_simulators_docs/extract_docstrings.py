import json
import logging
import re
from pathlib import Path

import click

@click.command()
@click.argument('source_file', type=click.Path(exists=True, path_type=Path))
@click.argument('output_file', type=click.Path(path_type=Path))
def extract_docstrings(source_file: Path, output_file: Path) -> None:
    logging.basicConfig(level=logging.INFO)
    docstrings = {}
    with open(source_file, 'r', encoding='utf_8') as file:
        content = file.read()
    pattern = re.compile(
        r'static constexpr char (\w+)\[\] = R"doc\((.*?)\)doc"\s*;',
        re.DOTALL
    )
    signature_pattern = re.compile(r'// Signature: (.*)')

    matches = pattern.findall(content)
    for match in matches:
        func_name, docstring_raw = match
        # Extract signature
        signature_match = signature_pattern.search(docstring_raw)
        signature = signature_match.group(1) if signature_match else None
        # Remove the signature line from the docstring
        docstring_processed = signature_pattern.sub('', docstring_raw).strip()

        if func_name.endswith('_docstring'):
            func_name_modified = func_name[:-len('_docstring')]
        else:
            func_name_modified = func_name

        # Organize the data to include both signature and docstring
        docstrings[func_name_modified] = {'signature': signature, 'doc': docstring_processed}

    with open(output_file, 'w', encoding='utf_8') as outfile:
        json.dump(docstrings, outfile, indent=4)
    logging.info(f"Extracted {len(docstrings)} docstrings from {source_file}")

if __name__ == "__main__":
    extract_docstrings()
