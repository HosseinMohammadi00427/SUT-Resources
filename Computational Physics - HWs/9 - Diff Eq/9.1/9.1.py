#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Euler method
import time
import numpy as np
import pylab as plb

plb.rcParams['figure.figsize'] = 8,6

Time_1 = time.time()

V = 10
C = 1e-6
R = 3e3

a,b = 0,5e-4
h = 5e-7
steps =int((b-a)//h) + 1
t0,y0 = 0,0
f_prim = lambda x,y : V/R - y/(R*C)
Qt = lambda t: C*V*(1-np.exp(-t/(R*C)))
Ys = [y0]

for i in range(1,steps):
    x = a+i*h
    Ys.append(Ys[-1] + h*f_prim(x,Ys[-1]))

plb.plot(np.linspace(a,b,steps),Ys,label="Euler Solution")
plb.plot(np.linspace(a,b,1000),(np.array([1]*1000)- np.exp(-np.linspace(a,b,1000)/(R*C)))*C*V,label="Analytical Solution")
plb.legend()

plb.title('Charge versus Time with \nR = {}\u03a9 , C = {}\u03bcF , V = {}v\nIn interval ({},{}) , h = {}'.format(R,C,V,a,b,h),fontsize=16)
plb.xlabel('Time',fontsize=15)
plb.ylabel('Q (charge)',fontsize=15)

print(time.time()-Time_1)

