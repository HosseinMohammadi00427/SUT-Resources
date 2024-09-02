#!/usr/bin/env python
# coding: utf-8

# In[4]:


import time
import numpy as np
import pylab as plb

plb.rcParams['figure.figsize'] = 8,6

Time_1 = time.time()

#Euler-Cromer method

a,b = 0,20*np.pi
h = 0.05
steps1 =int((b-a)//h) + 1
t0,x0,v0 = 0,0,2
f = lambda t,v : v
g = lambda t,x : -x 
Vs = [v0]
Xs1 = [x0]

for i in range(1,steps1):
    t = t0+i*h
    Vs.append(Vs[-1] + g(t,Xs1[-1])*h)
    Xs1.append(Xs1[-1] + f(t,Vs[-1])*h)
plb.figure(1)
plb.plot(np.linspace(a,b,steps1),Xs1)
#plb.plot(np.linspace(a,b,1000),2*np.sin(np.linspace(a,b,1000)))

plb.figure(2)
plb.plot(Xs1,Vs,label="Data points")
plb.legend()
plb.title('V versus X for Euler-Cromer\nh=0.05 and 10 cycles',fontsize=16)
plb.xlabel('X(Position)',fontsize=15)
plb.ylabel('V(elocity)',fontsize=15)


print(time.time()-Time_1)

