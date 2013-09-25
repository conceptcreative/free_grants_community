"""
# Ngram Analysis

Discover relevant phrases and terms.
"""

import csv
import argparse
from pprint import pprint
from StringIO import StringIO
from collections import Counter
from itertools import tee, islice

parser = argparse.ArgumentParser(description='Ngram Analyzer')

parser.add_argument('filename')
parser.add_argument('--skip-lines', type=int, default=1, help='number of lines to skip at the start of the file')
parser.add_argument('--drop-lines', type=int, default=1, help='number of lines to drop at the end of the file')
parser.add_argument('--column', default='Search term', help='name of the search term column')
parser.add_argument('--weight', default='Clicks', help='name of the column by which to weight terms')
parser.add_argument('--ngram-size', type=int, default=1, help='size of the ngram')
parser.add_argument('--display', type=int, default=10, help='number of ngrams to display')

args = parser.parse_args()

# Read file and parse lines.

with open(args.filename, 'rb') as fptr:
    data = list(csv.reader(fptr))

# Remove skipped/dropped lines.

data = data[args.skip_lines:-args.drop_lines]

# Parse header.

header = data[0]
data = data[1:]

term_pos = header.index(args.column)
weight_pos = header.index(args.weight)

# Aggregate statistics.

def ngrams(iterable, size):
    temp = iterable
    while True:
        alpha, beta = tee(temp)
        tup = tuple(islice(alpha, size))
        if len(tup) == size:
            yield tup
            next(beta)
            temp = beta
        else:
            break

counts = Counter()

for line in data:

    term = line[term_pos]
    weight = float(line[weight_pos])
    parts = term.split(' ')

    for subset in ngrams(parts, args.ngram_size):
        ngram = ' '.join(subset)
        counts[ngram] += weight

# Display statistics.

pprint(counts.most_common(args.display))
