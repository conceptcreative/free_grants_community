Go Free Government Money
========================

[GoFreeGovernmentMoney.com](http://www.gofreegovernmentmoney.com) ngram analysis.

Usage
-----

```
> python analyze.py --help
usage: analyze.py [-h] [--skip-lines SKIP_LINES] [--drop-lines DROP_LINES]
                  [--column COLUMN] [--weight WEIGHT]
                  [--ngram-size NGRAM_SIZE] [--display DISPLAY]
                  filename

Ngram Analyzer

positional arguments:
  filename

optional arguments:
  -h, --help            show this help message and exit
  --skip-lines SKIP_LINES
                        number of lines to skip at the start of the file
  --drop-lines DROP_LINES
                        number of lines to drop at the end of the file
  --column COLUMN       name of the search term column
  --weight WEIGHT       name of the column by which to weight terms
  --ngram-size NGRAM_SIZE
                        size of the ngram
  --display DISPLAY     number of ngrams to display
```
