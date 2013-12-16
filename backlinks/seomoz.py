"""
# Seomoz Backlink Analysis

Discover relevant backlinks.
"""

import os
import csv
import time
import argparse

import numpy as np
import pandas as pd

from lsapi import lsapi

api = lsapi('member-76bd0a8077', '09e78de0f24fbbf8b41b46623b75d5e6')

parser = argparse.ArgumentParser(description='Seomoz Analyzer')

parser.add_argument('urls', help='path to list of urls to analyze')
parser.add_argument('links', help='path to list of urls to output')
parser.add_argument('--column', default='resulturl', help='column name')

args = parser.parse_args()

urls = pd.read_csv(args.urls)
urls = set(urls[args.column])

if os.path.exists(args.links):
    df = pd.read_csv(args.links)
    for url in set(df['url']):
        urls.discard(url)
else:
    df = pd.DataFrame()

print 'Urls remaining:', len(urls)

data = list(df.loc[pos].to_dict() for pos in xrange(len(df)))

def write_links():
    global data
    print 'Writing', args.links
    with open(args.links, 'wb') as fptr:
        writer = csv.writer(fptr)
        header = ['lrid','lsrc','ltgt','luupa','luuu','upa','uu','url']
        writer.writerow(header)
        for row in data:
            cols = map(lambda val: row.get(val, ''), header)
            cols = [col if col != np.nan else '' for col in cols]
            writer.writerow(cols)

for pos, url in enumerate(urls):
    print 'Processing:', url
    try:
        results = api.links(url, filters=['external+follow'], scope='page_to_page', sort='page_authority', limit=100)
    except Exception as exc:
        print 'Exception', exc
        time.sleep(5)
        continue
    if results:
        for result in results:
            result['url'] = url
            data.append(result)
    else:
        data.append({'url': url})
    time.sleep(5)
    if pos % 5 == 0:
        write_links()

write_links()
