#!/usr/bin/env python
# coding: utf-8

# In[8]:


import time
import numpy as np
import pylab as plb

plb.rcParams['figure.figsize'] = 8,6

Time_1 = time.time()


#Velocity Verlet Algorithm

a,b = 0,20*np.pi
h = 0.001
steps3 =int((b-a)//h) + 1
t0,x0,v0 = 0,0,2

Acc = lambda x : -x

Vs = [v0]
Xs3 = [x0]

for i in range(1,steps3):
    t = t0+i*h
    Xs3.append(Xs3[-1] + Vs[-1]*h + 0.5*Acc(Xs3[-1])*(h**2))
    Vs.append(Vs[-1] + 0.5*h*( Acc(Xs3[-1]) + Acc(Xs3[-2])))
plb.plot(np.linspace(a,b,steps3),Xs3)
#plb.plot(np.linspace(a,b,1000),2*np.sin(np.linspace(a,b,1000)))

plb.figure(2)
plb.plot(Xs3,Vs)
plb.legend()
plb.title('V versus X for Velocity Verlet\nh=0.05 and 10 cycles',fontsize=16)
plb.xlabel('X(Position)',fontsize=15)
plb.ylabel('V(elocity)',fontsize=15)


print(time.time()-Time_1)

