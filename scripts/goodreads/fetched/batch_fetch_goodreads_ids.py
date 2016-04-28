# Assume that nytimes/fetched/bestseller-lists/**/*.json
# contains JSON files

from glob import glob
from os import makedirs
from os.path import join
from time import sleep
from book_foo import fetch_book_ids as apifetchbookids
import json
import sys
MAX_BATCH_SIZE = 100

INPUT_DATADIR = join('data', 'nytimes', 'fetched', 'bestseller-lists')
OUTPUT_DIR = join('data', 'goodreads', 'fetched')
OUTPUT_FILENAME = join(OUTPUT_DIR, 'isbn-to-goodreads-ids.csv')


def gather_unique_isbns(input_dir=INPUT_DATADIR):
    input_filenames = glob(join(input_dir, '**', '*.json'))
    isbns = []
    for fname in input_filenames:
        with open(fname, 'r') as rf:
            booksdata = json.load(rf)['results']['books']
        isbns.extend([b['primary_isbn13'] for b in booksdata])

    uniq_isbns = list(set(isbns))
    return uniq_isbns



def batch_fetch_book_ids(apikey, isbn_numbers):
    isbn_to_goodread_ids = []
    batch_nums = range(0, len(isbns), MAX_BATCH_SIZE)
    isbnbatches = [isbns[i:i+MAX_BATCH_SIZE] for i in batch_nums]
    for batchnum in range(0, len(isbns), MAX_BATCH_SIZE):
        # create a subslice of the list
        batch = isbns[batchnum:batchnum+MAX_BATCH_SIZE]
        resp = apifetchbookids(apikey, batch)
        yield (batch, resp)

if __name__ == '__main__':
    apikey = sys.argv[1]
    makedirs(OUTPUT_DIR, exist_ok=True)
    isbns = gather_unique_isbns(INPUT_DATADIR)
    print(len(isbns), 'unique isbn numbers')

    wf = open(OUTPUT_FILENAME, 'w')
    for i, (batch, resp) in enumerate(batch_fetch_book_ids(apikey, isbns)):
        # print(resp.url)
        gr_ids = resp.text.split(',')
        print('Batch number:', i, 'results:', len(gr_ids))
        for line in [','.join(z) for z in zip(batch, gr_ids)]:
           wf.write(line + '\n')
        sleep(2)
    print("Finished writing to", OUTPUT_FILENAME)
    wf.close()
