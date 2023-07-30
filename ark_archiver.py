#!/usr/bin/env python3

import os
import re
import sys
import unicodedata
from csv import reader
from weasyprint import HTML

source_csv = sys.argv[1] if len(sys.argv) > 1 else 'input.csv'
destination_dir = sys.argv[2] if len(sys.argv) > 2 else 'archive_pdfs'
destination_path = os.getcwd() + '/' + destination_dir

dest_exists = os.path.exists(destination_path)
if not dest_exists:
    os.makedirs(destination_path)

def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    # value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s;]+', '-', value).strip('-_')


with open(source_csv, 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        print('Working on: ' + destination_path + '/' + slugify(row[0]) + '.pdf')
        HTML(row[1]).write_pdf( destination_path + '/' + slugify(row[0]) + '.pdf')
        # HTML(row[1]).write_pdf(os.getcwd + '/' + destination_dir + '/' + slufigy(row[1]))

