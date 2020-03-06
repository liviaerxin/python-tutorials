import numpy as np
from matplotlib import pylab as pl

dataOne = np.random.randn(100)
dataTwo = np.random.randn(100)

hN = pl.hist(dataTwo, orientation='horizontal', normed=0, rwidth=0.8, label='ONE')
hS = pl.hist(dataOne, bins=hN[1], orientation='horizontal', normed=0, 
    rwidth=0.8, label='TWO')


for p in hS[2]:
    print(p)
    p.set_width( - p.get_width())

xmin = min([ min(w.get_width() for w in hS[2]), 
                min([w.get_width() for w in hN[2]]) ])
xmin = np.floor(xmin)
xmax = max([ max(w.get_width() for w in hS[2]), 
                max([w.get_width() for w in hN[2]]) ])
xmax = np.ceil(xmax)
range = xmax - xmin
delta = 0.0 * range
pl.xlim([xmin - delta, xmax + delta])
xt = pl.xticks()
n = xt[0]
s = ['%.1f'%abs(i) for i in n]
pl.xticks(n, s)
pl.legend(loc='best')
pl.axvline(0.0)
pl.show()