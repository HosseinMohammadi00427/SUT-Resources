#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
plt.rcParams['figure.figsize'] = 12,8


width, height = 500,500
c = complex(0,-1)
r = 4
itmax = 100
xmin, xmax = -1.5, 1.5
xwidth = xmax - xmin
ymin, ymax = -1.5, 1.5
yheight = ymax - ymin

julia = np.zeros((width, height))
for ix in range(width):
    for iy in range(height):
        nit = 0

        z = complex(
                    iy /height * yheight + ymin,ix / width * xwidth + xmin)

        while abs(z) <= r and nit < itmax:
            z = z**2 + c
            nit += 1
        ratio = nit / itmax
        julia[ix,iy] = ratio


plt.imshow(julia, cmap=cm.prism)

plt.show()

