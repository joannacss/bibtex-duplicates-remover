# pipenv run python3.9 bib.py
# pipenv install -r requirements.txt
from pybtex.database.input import bibtex
from pybtex.database import BibliographyDataError
from Levenshtein import distance
import sys

THRESHOLD = 5

def main():
    all_entries = dict()
    for bibfile in sys.argv[1:]:
        print("==============")
        print("PARSING", bibfile)
        try:
            parser = bibtex.Parser()
            bibdata = parser.parse_file(bibfile)

            for bib_id in bibdata.entries:
                fields = bibdata.entries[bib_id].fields
                all_entries[bib_id] = fields["title"]
        except BibliographyDataError as e:
            print(e)

    for src in all_entries:
        for tgt in all_entries:
            if src != tgt:
                edit_distance = distance(all_entries[src], all_entries[tgt])
                if edit_distance <= THRESHOLD:
                    print("POSSIBLE DUPLICATES")
                    print("\t",src,all_entries[src])
                    print("\t",tgt,all_entries[tgt])

    # print(all_entries)


if __name__ == '__main__':
    main()
