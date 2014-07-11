import requests, argparse, sys
import simplejson as json
from urllib import quote_plus

parser = argparse.ArgumentParser(description='Compare Two Queries')

parser.add_argument('--term', action='append')

args = parser.parse_args()

if len(args.term) == 0:
    sys.exit(1)

def avg(values):
    total = 0.0
    count = 0
    for value in values:
        total += value
        count += 1
    return total / count

url = 'http://www.google.com/trends/fetchComponent?q={0}&cid=TIMESERIES_GRAPH_0&export=3'

terms = ['grants for students', 'grants for teachers']
sess = requests.Session()
resp = sess.get('http://www.google.com/trends/',
                headers={'User-Agent': 'Mozilla/5.0'})
resp = sess.get(url.format(','.join(quote_plus(term) for term in terms)),
                headers={'User-Agent': 'Mozilla/5.0'})
with open('temp.html', 'w') as fptr:
    fptr.write(resp.text)
text = resp.text
text = text[:-2]
text = text[62:]
text = text.replace('new Date(', '[')
text = text.replace(')', ']')
data = json.loads(text)

avgs = [avg(row['c'][pos + 1]['v'] for row in data['table']['rows'][-6:])
        for pos in xrange(len(terms))]

print zip(terms, avgs)
