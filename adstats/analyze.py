"""
# Adstats Analysis

Calculate and display statistics based on ad network data.
"""

import argparse
import pandas as pd
import matplotlib.pyplot as plt
from StringIO import StringIO

parser = argparse.ArgumentParser(description='Ad Network Statistics')

parser.add_argument('--adwords', type=str, help='path to Google Adwords csv report')
parser.add_argument('--adsense', type=str, help='path to Google Adsense csv report')
parser.add_argument('--print-col-names', action='store_true', default=False)
parser.add_argument('--interactive', action='store_true', default=False)

args = parser.parse_args()

adwords = pd.read_csv(args.adwords, skiprows=1, skipfooter=1, thousands=',',
                      parse_dates=[0,], index_col=0)
adwords['CTR'] = adwords['CTR'].map(lambda val: float(val[:-1]) / 100)
adwords.rename(columns=lambda val: 'Adwords ' + val, inplace=True)

text = open(args.adsense, 'rb').read().decode('utf-16').encode('utf-8')
adsense = pd.read_csv(StringIO(text), sep=None, parse_dates=[0,],
                      index_col=0)
adsense['Page CTR'] = adsense['Page CTR'].map(lambda val: float(val[:-1]) / 100)
adsense.rename(columns=lambda val: 'Adsense ' + val, inplace=True)

data = pd.merge(adwords, adsense, left_index=True, right_index=True)
data['Profit'] = data['Adsense Estimated earnings (USD)'] - data['Adwords Cost']

if args.print_col_names:
    for idx, name in enumerate(data.columns):
        print '{0} "{1}"'.format(idx, name)

if args.interactive:
    import pylab
    pylab.ion()
    from IPython import embed
    embed()
