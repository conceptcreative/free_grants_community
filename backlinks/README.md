Backlinks Analysis Based on Seomoz API
======================================

[Free Grants Community](http://www.gofreegovernmentmoney.com) backlinks analysis based on the Seomoz API.

How-To Setup
------------

```
import numpy as np
import pandas as pd
results = pd.read_csv('results.clean.csv')
results['suffix'] = [domain[domain.rindex('.'):] if not pd.isnull(domain) else np.nan for domain in results['domain']]
competitors = results[(results['suffix'] == '.com') | (results['suffix'] == '.org') | (results['suffix'] == '.us') | (results['suffix'] == '.net')]

page = 9
prev = competitors[competitors['page'] < page]['resulturl'].copy()
prev = prev.drop_duplicates()
urls = competitors[competitors['page'] == page]['resulturl'].copy()
urls = urls.drop_duplicates()
prev = set(prev.values.tolist())
urls = set(urls.values.tolist())
urls = pd.DataFrame(list(urls - prev))
urls.to_csv('urls.page-0{}.csv'.format(page), header='url')
urlsname = 'urls.page-0{}.csv'.format(page)
linksname = 'links.page-0{}.csv'.format(page)
!python seomoz.py $urlsname $linksname
```

How-To Analyze
--------------

```
import tldextract
import numpy as np
import pandas as pd

from urlparse import urlparse
from collections import Counter

data = pd.read_csv('links.page-01.csv')
data['uubase'] = ['.'.join(tldextract.extract(urlparse(url).path)) if not pd.isnull(url) else np.nan for url in data['uu']]
data['urlbase'] = ['.'.join(tldextract.extract(urlparse(url).path)) if not pd.isnull(url) else np.nan for url in data['luuu']]
```

Most Important Article Directories
----------------------------------

```
uus = [tup[0] for tup in Counter(data['uu']).most_common(50)]
writer.writerows(Counter(dict(                                                \
    (uus[pos], len(set(data[data['uu'] == uus[pos]]['urlbase'])))             \
    for pos in xrange(len(uus)))).most_common(45))
```

Other Interesting Data
----------------------

```
links = api.links('moz.com', filters=['external+follow'], scope='domain_to_page', sort='domain_authority', limit=20)
links = api.links('moz.com', filters=['external+follow'], scope='domain_to_subdomain', sort='domain_authority', limit=100)
```
