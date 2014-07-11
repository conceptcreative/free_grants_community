import argparse, os, sys, csv, heapq, string
from automaton import *
from bs4 import BeautifulSoup

done = set()

parser = argparse.ArgumentParser(description='Crawl Google Auto-Complete Query')

parser.add_argument('filename')
parser.add_argument('--query', action='append')
parser.add_argument('--prefix', action='append')
parser.add_argument('--include', action='append')
parser.add_argument('--exclude', action='append')

args = parser.parse_args()

if args.query:
    queries = list(args.query)
else:
    queries = [letter for letter in string.lowercase]

if os.path.exists(args.filename):
    with open(args.filename, 'rb') as fptr:
        for line in csv.reader(fptr):
            query = line[0]
            result = line[1]
            done.add(query)
            heapq.heappush(queries, result[:(len(query) + 1)])

print 'Crawled:', len(done)

comm = connect()
comm.setup()
comm.visit('http://www.google.com')
comm.wait()

lines = ['var el = document.getElementById("gbqfq");',
         'el.focus();',
         'var evt = document.createEvent("KeyboardEvent");',
         'evt.initKeyboardEvent ("keypress", true, true, window, 0, 0, 0, 0, 0, "a".charCodeAt(0));']

for line in lines:
    comm.Runtime.evaluate(expression=line)

comm.wait()

with open(args.filename, 'ab') as fptr:
    data = csv.writer(fptr)
    
    while queries:
        query = heapq.heappop(queries)
    
        if query in done:
            continue
        if args.prefix:
            if not any(query.startswith(prefix) for prefix in args.prefix):
                continue
        if args.include:
            if not any(inc in query for inc in args.include):
                continue
        if args.exclude:
            if any(exc in query for exc in args.exclude):
                continue
    
        comm.Runtime.evaluate(expression='el.value = "{0}";'.format(query))
        comm.Runtime.evaluate(expression='el.dispatchEvent(evt);')
    
        soup = BeautifulSoup(comm.html())
    
        try:
            # TODO: This will fail on:
            # "adding google calendar to microsoft o..."
            # Google changes the html structure for long queries.
    
            options = [el.find('td').text for el in soup.findAll(attrs={'class': 'gssb_a gbqfsf'})]
    
            done.add(query)

            print query

            for option in options:
                data.writerow([query, option])
    
            for option in options:
                heapq.heappush(queries, option[:(len(query) + 1)])
        except:
            pass
