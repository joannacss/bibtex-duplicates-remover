# pip install bibtexparser

import argparse

# import bibtexparser
# from bibtexparser.bparser import BibTexParser
from pybtex.database.input import bibtex


# def select_entries_by_id(bibtex_file, entry_ids):
#     with open(bibtex_file, 'r') as file:
#         bibtex_str = file.read()
#
#     parser = BibTexParser(common_strings = True)
#     parser.bib_database.load_common_strings()
#     bib_database = bibtexparser.loads(bibtex_str, parser)
#     selected_entries = []
#
#     for entry in bib_database.entries:
#         if entry['ID'] in entry_ids:
#             selected_entries.append(entry)
#
#     return selected_entries

# def format_bibtex_entry(entry):
#     # return a string representation of the bib entry
#
#     formatted_entry = '@' + entry['ENTRYTYPE'] + '{' + entry['ID'] + ',\n'
#     for key, value in entry.items():
#         if key not in ['ENTRYTYPE', 'ID']:
#             formatted_entry += '    ' + key + ' = {' + value + '},\n'
#     formatted_entry += '}\n'
#
#     return formatted_entry


def select_entries_by_id(bibtex_file, entry_ids):
    selected_entries = []
    try:
        parser = bibtex.Parser()
        bibdata = parser.parse_file(bibtex_file)

        for bib_id in bibdata.entries:
            if bib_id in entry_ids:
                selected_entries.append(bibdata.entries[bib_id])
    except Exception as e:
        print(e)
    return selected_entries


def format_bibtex_entry(entry):
    # return a string representation of the bib entry
    return entry.to_string('bibtex')


def read_ids(filepath: str) -> list:
    '''
    Read a file containing a list of entry IDs, one per line
    :param filepath: full path to the text file
    :return: a list of BibTex IDs
    '''
    with open(filepath, 'r') as file:
        ids = file.read().splitlines()
    return ids


if __name__ == '__main__':

    # use argparse to parse program arguments like this file1.bib file2.bib --ids id1 id2
    parser = argparse.ArgumentParser(description='Filter BibTeX entries by ID')
    # path to your BibTeX file
    parser.add_argument('bibtex_filepath')  # positional argument
    # path to your text file with IDs (one ID per line)
    parser.add_argument('ids_filepath')  # positional argument
    args = parser.parse_args()

    # get arguments
    bibtex_file = args.bibtex_filepath  # '/Users/joanna/Documents/Portfolio/GitHub/joannacss/gists/refs.bib'
    entry_ids = read_ids(args.ids_filepath)

    selected_entries = select_entries_by_id(bibtex_file, entry_ids)

    # Print the selected entries
    for entry in selected_entries:
        # if 'doi' in entry.fields:
        #     print(entry.key, entry.fields["doi"], sep='\t')
        print(format_bibtex_entry(entry))
