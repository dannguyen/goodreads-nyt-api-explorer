from glob import glob
from os import makedirs
from os.path import join
import csv
import json

from bestseller_list import extract_rankings
from bestseller_list import RANKING_HEADERS


IN_DATA_DIR = join('data', 'nytimes', 'fetched', 'bestseller-lists')
OUT_DATA_DIR = join('data', 'nytimes', 'wrangled', 'rankings')
makedirs(OUT_DATA_DIR, exist_ok=True)

LIST_NAMES = ['combined-print-and-e-book-fiction', 'combined-print-and-e-book-nonfiction']

for listname in LIST_NAMES:
    rankings = []
    in_filenames = glob(join(IN_DATA_DIR, listname, '*.json'))
    print("Reading listname:", listname, 'with:', len(in_filenames), 'files')
    for fn in in_filenames:
        with open(fn, 'r') as rf:
            apidata = json.load(rf)
            try:
                x = extract_rankings(apidata)
                rankings.extend(x)
            except Exception as err:
                print(err)
    print("Collected", len(rankings), 'rankings.')
    out_filename = join(OUT_DATA_DIR, '{n}.csv'.format(n=listname))
    print("Writing to:", out_filename)
    with open(out_filename, 'w') as wf:
        c = csv.DictWriter(wf, fieldnames=RANKING_HEADERS)
        c.writeheader()
        c.writerows(rankings)
