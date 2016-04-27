# Todo

Changing ISBN numbers to goodreads IDs


# NYTimes API

http://developer.nytimes.com/apps/mykeys

http://developer.nytimes.com/docs/read/best_sellers_api#h2-examples

## Best sellers list

HTML URL:
  http://www.nytimes.com/best-sellers-books/2015-01-01/combined-print-and-e-book-fiction/list.html

API_URL:
  http://api.nytimes.com/svc/books/v3/lists/2015-01-01/combined-print-and-e-book-fiction.json?api-key=NYTIMES_DEV_KEY



# Goodreads API


## Show book

HTML URL:
  https://www.goodreads.com/book/show/4671

endpoint: 
  /book/show.xml
sample:
  http://www.goodreads.com/book/show.xml?id=4671&key=YOUR_DEV_KEY

| key | sample value |    description     |
|-----|--------------|--------------------|
| id  | 4671         | Goodreads book ID |
| key | YOUR_DEV_KEY | your developer key |



## Review counts

endpoint: 
  /book/review_counts.json

sample:
  https://www.goodreads.com/book/review_counts.json?isbns=9780441172719,9780140449181



|  key  |         sample value        | description |
|-------|-----------------------------|-------------|
| isbns | 9780441172719,9780140449181 |             |


