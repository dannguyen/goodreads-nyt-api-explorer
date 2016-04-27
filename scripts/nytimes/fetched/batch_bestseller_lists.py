from bestseller_foo import fetch_list
from dateutil import rrule
from datetime import datetime, timedelta
from os import makedirs
from os.path import join, realpath
import json
import sys # for the exit

def generate_weekdate_strings(ymd_start, ymd_end):
    dx = datetime.strptime(ymd_start, '%Y-%m-%d')
    dy = datetime.strptime(ymd_end, '%Y-%m-%d')
    date_iterator = rrule.rrule(rrule.WEEKLY, dtstart=dx, until=dy)
    dates = [dt.strftime('%Y-%m-%d') for dt in date_iterator]
    return dates


if __name__ == '__main__':
    api_key = input("Please type API key and hit Enter: ")
    if not api_key:
        raise ValueError('API Key cannot be blank')

    _dval = 'combined-print-and-e-book-fiction'
    listname = input('Enter NYT bestsellers list name (default: %s): ' % _dval)
    if not listname:
        listname = _dval

    _dval = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
    starting_date = input('Enter starting date (default: %s): ' % _dval)
    if not starting_date:
        starting_date = _dval

    _dval = datetime.now().strftime('%Y-%m-%d')
    ending_date = input('Enter ending date (default: %s): ' % _dval)
    if not ending_date:
        ending_date = _dval

    _dval = realpath(join('data', 'nytimes', 'fetched', 'bestseller-lists', listname))
    savetodir = input('Enter absolute path to save to (default: %s): ' % _dval)
    if not savetodir:
        savetodir = _dval
    makedirs(savetodir, exist_ok=True)

    # generate dates
    weekdates = generate_weekdate_strings(starting_date, ending_date)

    print("Best-seller list:", listname)
    print("From:", weekdates[0])
    print("To:", weekdates[1])
    print("Weeks:", len(weekdates))
    print("Saving to:", savetodir)

    print("\n\n\n")
    is_ok = input("OK? (enter 'Y' to confirm; anything else cancels) ")

    if is_ok != 'Y':
        print("Quitting...")
        sys.exit()

    for i, dt in enumerate(weekdates):
        print("\n")
        print(dt, '({ith}/{count})'.format(ith=i+1, count=len(weekdates)))
        resp = fetch_list(api_key=api_key, date=dt, list_name=listname)
        print(" Fetching URL:")
        print("\t", resp.url)

        if resp.status_code != 200:
            print("Exiting!")
            print("Status code is:", resp.status_code)
            print("Text dump:")
            print(resp.text)
            sys.exit()
        fname = join(savetodir, '{date}.json'.format(date=dt))
        with open(fname, 'w') as f:
            # pretty format it
            txt = json.dumps(resp.json(), indent=2)
            print(" Saving to:")
            print("Saving", len(txt), 'characters to:')
            print('\t', fname)
            f.write(txt)


