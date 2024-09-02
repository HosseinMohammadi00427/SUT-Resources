#!/usr/bin/env python
# coding: utf-8

# In[12]:


import time
import numpy as np
import pylab as plb

plb.rcParams['figure.figsize'] = 8,6

Time_1 = time.time()


V = 10
C = 0.1
R = 9.5


a,b = 0,6
h = 0.1
steps =int((b-a)//h) + 1
t0,y0 = 0,C*V
f_prim = lambda x,y : -y/(R*C)
Qt = lambda t: C*V*(np.exp(-t/(R*C)))
Ys = [y0,y0+h*f_prim(a+h,y0)]

for i in range(1,steps):
    x = a+i*h
    Ys.append(Ys[-2] + 2*h*f_prim(x,Ys[-1]))

plb.plot(np.linspace(a,b,steps+1),Ys,label="Euler Solution")
plb.plot(np.linspace(a,b,1000),(np.exp(-np.linspace(a,b,1000)/(R*C)))*C*V,label="Analytical Solution")
plb.legend()
plb.title('Capacitor In De-charging Mode\nR = {}\u03a9 , C = {}\u03bcF , V = {}v\nIn interval ({},{}) , h = {}'.format(R,C,V,a,b,h),fontsize=16)
plb.xlabel('t (Time)',fontsize=15)
plb.ylabel('Q(Charge)',fontsize=15)

print(time.time()-Time_1)

