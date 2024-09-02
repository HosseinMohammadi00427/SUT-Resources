from graphics import *
import math
import random

def Contraction(x,y):
    return 0.5*x,0.5*y
def RightMovement(x,y):
    return 0.5*x+0.5,0.5*y
def UpMovement(x,y):
    return 0.5*x+0.25,0.5*y+0.5*math.sqrt(3)/2

x,y =[],[]

Level=50
Iteration = 50000

for j in range(Iteration):
    a = random.random() # in range [0,1]
    b = random.random() # in range [0,1]
    # like a square ...
    for k in range(Level):
        f = random.choice([Contraction,RightMovement,UpMovement])
        a,b = f(a,b)
    x += [a]
    y += [b]

win = GraphWin("Random Algorithm", 600,600)
for j in range(Iteration):
    po = Point(600-x[j]*600,600-y[j]*600)
    po.setFill('blue')
    po.draw(win)
win.getMouse()
win.close()