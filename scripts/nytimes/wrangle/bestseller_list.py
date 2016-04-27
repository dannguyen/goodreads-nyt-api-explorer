BASIC_BOOK_HEADERS = ['rank', 'primary_isbn13',
                      'rank_last_week', 'weeks_on_list']
RANKING_HEADERS = BASIC_BOOK_HEADERS + ['list_date', 'list_name', 'rank_change']

def extract_rankings(apidata):
    """
    apidata is a parsed data object (a dict), in the expected
        api format

    returns a list of dicts:

    each dict looks like:
         {'list_date': '2015-01-03',
         'list_name': 'combined-print-and-e-book-fiction',
         'primary_isbn13': '9780698138636',
         'rank': 3,
         'rank_change': -3,
         'rank_last_week': 6,
         'weeks_on_list': 17}
    """
    listdata = apidata['results']
    bookdata = listdata['books']
    rankings = []
    for book in bookdata:
        d = {'list_date': listdata['bestsellers_date'],
             'list_name': listdata['list_name_encoded']}
        for h in BASIC_BOOK_HEADERS:
            d[h] = book[h]
        d['rank_change'] = d['rank'] - d['rank_last_week']
        rankings.append(d)
    return rankings


