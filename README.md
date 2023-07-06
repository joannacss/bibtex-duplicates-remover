# Overview

Several tools for working with BibTeX files.

- `find_duplicates.py`: This script finds duplicated entries in bib text file(s).
- `filter_entries.py`: Given a list of bibtex IDs, it filters out entries from a bib text file.

## Usage

### Removing duplicated entries (find_duplicates.py)

```
pipenv install -r requirements.txt
pipenv run python3.9 find_duplicates.py file1.bib file2.bib ...
```

### Filtering entries (filter_entries.py)

```
pipenv install -r requirements.txt
pipenv run python3.9 filter_entries.py /path/to/file.bib /path/to/ids.txt
```

The `file.bib` is your bibtex file to be parsed, whereas the `ids.txt` is the path to a text file containing a list of
BibTex entry IDs (one per line). 



