Adstats Analysis
================

[Free Grants Community](http://www.gofreegovernmentmoney.com) ad network statistics analysis.

Plots
-----

Comparing Day / Week / Month Profits
....................................

```
data['Profit'].plot()
data.resample('W', how='mean')['Profit'].plot()
data.resample('M', how='mean')['Profit'].plot()
pylab.legend(['Day', 'Week', 'Month'])
pylab.ylabel('Profit')
pylab.title('Plot of Profit by Day / Week / Month')
```

Comparing Day of Week Profits
.............................

```
data.asfreq(freq='W-SUN')['Profit'].plot()
data.asfreq(freq='W-MON')['Profit'].plot()
data.asfreq(freq='W-TUE')['Profit'].plot()
data.asfreq(freq='W-WED')['Profit'].plot()
data.asfreq(freq='W-THU')['Profit'].plot()
data.asfreq(freq='W-FRI')['Profit'].plot()
data.asfreq(freq='W-SAT')['Profit'].plot()
pylab.legend(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
pylab.ylabel('Profit')
pylab.title('Plot of Profit by Day of Week')
```

Boxplot for Day of Week Profits
...............................

```
dow = pd.DataFrame(data={day: data.asfreq(freq='W-' + day)['Profit'] for day in pd.datetools.DAYS}, columns=pd.datetools.DAYS)
dow.boxplot()
pylab.ylabel('Profit')
pylab.title('Boxplot of Profit by Day of Week')
```

Usage
-----

```
> python analyze.py --help
usage: analyze.py [-h] [--adwords ADWORDS] [--adsense ADSENSE]
                  [--print-col-names] [--interactive]

Ad Network Statistics

optional arguments:
  -h, --help         show this help message and exit
  --adwords ADWORDS  path to Google Adwords csv report
  --adsense ADSENSE  path to Google Adsense csv report
  --print-col-names
  --interactive
```
