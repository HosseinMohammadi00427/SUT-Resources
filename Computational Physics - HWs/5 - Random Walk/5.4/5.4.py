#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pylab as plb

p = 0.38
q = 1-p
p_non_existence = 0.01
SIZE = 21
Places0 = range(-SIZE//2+1,SIZE//2+1)
N=0
Places = np.zeros(SIZE)
xData = []
yData = []

for Pl0 in Places0:
    N=0
    Places = np.zeros(SIZE)
    Places[Pl0 + SIZE//2] = 1
    while np.sum(Places) > p_non_existence:

        avail_homes = np.argwhere(Places)
        for av in avail_homes:
            if av == 0:
                Places[av+1] += p*Places[av]
            elif av == SIZE-1:
                Places[av-1] += q*Places[av]
            else:
                Places[av-1] += q*Places[av]
                Places[av+1] += p*Places[av]
            Places[av] = 0
        N+=1
    xData.append(Pl0)
    yData.append(N)

plb.plot(xData,yData,linestyle = "--",label='connected data points')

plb.title('the distribution of Age versus first Place \nfor p = {}'.format(p))
plb.legend()
plb.xlabel('Pl0 (Where the walker was at t=0)',fontsize=16)
plb.ylabel('Age (Calculated by provided method)',fontsize=16)

