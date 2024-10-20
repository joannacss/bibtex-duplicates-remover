"""
This is a script to find all references being cited in a latex file.
It identifies those and generate another bibfile that only include these citations.
"""
import argparse
from pybtex.database.input import bibtex
import re
import os



def select_entries_by_id(bibtex_file, entry_ids):
    selected_entries = []
    try:
        parser = bibtex.Parser()
        bibdata = parser.parse_file(bibtex_file)

        for bib_id in bibdata.entries:
            if bib_id in entry_ids:
                selected_entries.append(bibdata.entries[bib_id])
    except Exception as e:
        print("error",e)
    return selected_entries


def format_bibtex_entry(entry):
    # return a string representation of the bib entry
    return entry.to_string('bibtex')


def extract_citations(latex_file:str)->set:
    """Extract citations from LaTeX file."""
    citations = set()

    with open(latex_file, 'r') as file:
        content = file.read()

    # Match \cite commands in LaTeX
    citation_pattern = r'\\cite\{(.*?)\}'
    matches = re.findall(citation_pattern, content)

    # Flatten matches and remove duplicates
    for m in matches:
        citations.update(m.split(','))

    # Remove leading/trailing spaces and return as a set
    return set(cite.strip() for cite in citations)


if __name__ == '__main__':

    # use argparse to parse program arguments like this file1.bib file2.bib --ids id1 id2
    # parser = argparse.ArgumentParser(description='Filter BibTeX entries by ID')
    # # path to your BibTeX file
    # parser.add_argument('bibtex_filepath')  # positional argument
    # # path to your text file with IDs (one ID per line)
    # parser.add_argument('ids_filepath')  # positional argument
    # args = parser.parse_args()

    # get arguments
    # bibtex_file = args.bibtex_filepath  # '/Users/joanna/Documents/Portfolio/GitHub/joannacss/gists/refs.bib'
    # entry_ids = extract_citations(args.ids_filepath)
    bibtex_file = 'refs.bib'
    latex_file = 'main.tex'
    entry_ids = extract_citations(latex_file)

    selected_entries = select_entries_by_id(bibtex_file, entry_ids)

    # Save the selected entries
    with open("output.bib", "w") as f:
        for entry in selected_entries:
            f.write(format_bibtex_entry(entry))
            f.write("\n\n")

    print("Selected entries saved to output.bib")
