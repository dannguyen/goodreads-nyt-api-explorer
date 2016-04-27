import requests
API_ENDPOINT = 'http://api.nytimes.com/svc/books/v3'
LISTS_PATH = '/lists/{weekdate}/{listname}.json'
def fetch_list(api_key, list_name, date):
    """
    arguments:
        `api_key` is NYT API key

        `list_name` is the canonical name for best sellers list,
            e.g. 'combined-print-and-e-book-fiction'

        `date` is in YYYY-MM-DD format
            e.g. '2015-01-01'

    returns:
        A requests.Response object...
            let the calling user decide what to extract from it
    """

    myparams = {'api-key': api_key}
    mypath = LISTS_PATH.format(weekdate=date, listname=list_name)
    myurl = API_ENDPOINT + mypath
    resp = requests.get(myurl, myparams)
    return resp
