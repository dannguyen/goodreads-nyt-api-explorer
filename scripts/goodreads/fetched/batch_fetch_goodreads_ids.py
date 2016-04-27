# Assume that nytimes/fetched/bestseller-lists/**/*.json
# contains JSON files

from glob import glob
from os.path import join
from time import sleep
from book_foo import fetch_book_ids
import json
MAX_BATCH_SIZE = 100

INPUT_DATADIR = join('data', 'nytimes', 'fetched', 'bestseller-lists')
OUTPUT_FILENAME = join(OUTPUT_DIR, 'isbn-to-goodreads-ids.csv')

def fetch_and_save_book_ids(apikey, input_dir, output_filename):
    input_filenames = glob(join(input_dir, '**', '*.json'))

    isbns = []
    for fname in input_filenames:
        with open(fname, 'r') as rf:
            booksdata = json.load(rf)['results']['books']
        isbns.extend([b['primary_isbn13'] for b in booksdata])

    print('Total isbn numbers', len(isbns))
    uniq_isbns = list(set(isbns))
    print('Unique isbn numbers', len(uniq_isbns))

    batch_nums = range(0, len(uniq_isbns), MAX_BATCH_SIZE)
    isbnbatches = [uniq_isbns[i:i+MAX_BATCH_SIZE] for i in batch_nums]


    isbn_to_goodread_ids = []
    for batchnum in range(0, len(uniq_isbns), MAX_BATCH_SIZE):
        # create a subslice of the list
        batch = uniq_isbns[batchnum:batchnum+MAX_BATCH_SIZE]
        print('Batch number:', batchnum, batch[0], '...to...', batch[-1])
        resp = fetch_book_ids()


