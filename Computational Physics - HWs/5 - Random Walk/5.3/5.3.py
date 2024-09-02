#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pylab as plb
import random


N = 0
p = 0.5

iterations = 5000
SIZE = 20
Places0 = range(-SIZE//2,SIZE//2+1)
N_vals = []
xData = []
yData = []

for Pl0 in Places0:
    N_vals =[]
    for _ in range(iterations):

        N,Place=0,Pl0

        while 1:
            rand_num = random.random()
            if rand_num<p:
                Place +=1
                N+=1
            else:
                Place -=1
                N+=1

            if( abs(Place) > SIZE//2 ):
                break
        N_vals.append(N)
    xData.append(Pl0)
    yData.append(np.mean(np.array(N_vals)))

        



plb.plot(xData,yData,linestyle = "--",label='connected data points')

plb.title('the distribution of Mean age versus first Place \nfor {} iteration and {} Places with p = {}'.format(iterations,SIZE,p))
plb.legend()
plb.xlabel('Pl0 (Where the walker was at t=0)',fontsize=16)
plb.ylabel('Mean Age (N_mean)',fontsize=16)

