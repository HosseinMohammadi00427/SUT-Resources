#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
from PIL import Image

pts = 100000

class Fern(object):
    def __init__(self, img_width, img_height, c=(0, 0, 0),
                 bg_color=(255, 255, 255)):
        self.img_width, self.img_height = img_width, img_height
        self.paint_color = c
        self.x, self.y = 0, 0
        self.i = 0
 
        self.fern = Image.new('RGB', (img_width, img_height), bg_color)
        self.pix = self.fern.load()
        self.pix[self.scale(0, 0)] = c
 
    def scale(self, x, y):
        h = (x + 2.182)*(self.img_width - 1)/4.8378
        k = (9.9983 - y)*(self.img_height - 1)/9.9983
        return h, k
 
    def transform(self, x, y):
        rand = random.uniform(0, 100)
        if rand < 1:
            return 0, 0.16*y
        elif 1 <= rand < 86:
            return 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6
        elif 86 <= rand < 93:
            return 0.18*x - 0.26*y, 0.23*x + 0.22*y + 1.6
        else:
            return -0.15*x + 0.28*y, 0.2*x + 0.25*y + 0.44
 
    def iterate(self, j):
        for t in range(j):
            self.x, self.y = self.transform(self.x, self.y)
            self.pix[self.scale(self.x, self.y)] = self.paint_color
        self.i += j
        self.fern.show()
        
 
fern = Fern(500,500)
fern.iterate(pts)
 

