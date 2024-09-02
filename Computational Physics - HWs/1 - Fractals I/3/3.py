from graphics import *
import math
width = 600
height = 600
lvl = 4
def Contraction(x,y):
    return width/2+0.5*x,height/2 + 0.5*y
def RightMovement(x,y):
    return 0.5*x+0.25*width,0.5*y+height/15
def UpMovement(x,y):
    return 0.5*x+0*0.25*width,0.5*y+0.5*math.sqrt(3)/2*height +height/15
def Transformation(x,y):
    return x*width,height-y*height
def inv_Transformation(x,y):
    return x/width,+1-y/height
def serpinski(Pts,lvl):
    if lvl == 0 :
        return Pts
    for k in range(lvl):
        new_Pts_I = []
        new_Pts_II = []
        new_Pts_III = []
        for P in Pts:
            new_Pts_I.append(inv_Transformation(*Contraction(*Transformation(*P))))
            new_Pts_II.append(inv_Transformation(*RightMovement(*Transformation(*P))))
            new_Pts_III.append(inv_Transformation(*UpMovement(*Transformation(*P))))
        Pts = new_Pts_I + new_Pts_II +new_Pts_III
    return Pts

Pts = [(0,0),(1,0),(1/2,math.sqrt(3)/2)]
Pts = serpinski(Pts,lvl)
Points =[Point(*Transformation(*P)) for P in Pts]

win = GraphWin("Serpinski Algorithm", width,height)

for i in range(0,len(Points),3):
    po = Polygon(Points[i],Points[i+1],Points[i+2])
    po.setFill('blue')
    po.setOutline('black')
    po.draw(win)
win.getMouse()
win.close()