#!/usr/bin/env python
# coding: utf-8

# In[10]:


import time
import numpy as np
import pylab as plb

plb.rcParams['figure.figsize'] = 8,6

Time_1 = time.time()



#Beeman algorithm

a,b = 0,20*np.pi
h = 0.05
steps4 =int((b-a)//h) + 1
t0,x0,v0 = 0,0,2
x1 = v0*h
Acc = lambda x : -x

Vs = [v0]
Xs4 = [x0,x1]

for i in range(1,steps4):
    t = t0+i*h
    Xs4.append(Xs4[-1] + Vs[-1]*h + (1/6)*(4*Acc(Xs4[-1]) - Acc(Xs4[-2]))*(h**2))
    Vs.append(Vs[-1] +(1/6)*(2*Acc(Xs4[-1]) + 5*Acc(Xs4[-2]) - Acc(Xs4[-3]))*h )
plb.plot(np.linspace(a,b,steps4+1),Xs4)
#plb.plot(np.linspace(a,b,1000),2*np.sin(np.linspace(a,b,1000)))

plb.figure(2)
plb.plot(Xs4[:-1],Vs)
plb.legend()
plb.title('V versus X for Beeman\nh=0.05 and 10 cycles',fontsize=16)
plb.xlabel('X(Position)',fontsize=15)
plb.ylabel('V(elocity)',fontsize=15)


print(time.time()-Time_1)

