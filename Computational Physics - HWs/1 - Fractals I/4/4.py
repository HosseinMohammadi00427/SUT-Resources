old_pasc = [1]
new_pasc = []
k = 512   
width = 700
height = 700
spaces = 2  
win = GraphWin("Serpinski", width,height)
for i in range(k-1):
    n = len(old_pasc)
    for j in range(0,n-1):
        new_pasc.append(old_pasc[j]+old_pasc[j+1])
    new_pasc.insert(len(new_pasc),1)
    new_pasc.insert(0,1)
    for m,pasc in enumerate(new_pasc):
        MID = int(n/2)
        if(n%2 and pasc%2):
            P = Point(width/2 + (m-MID)*spaces,i*2)
            P.draw(win)
        elif(pasc%2):
            P = Point(width/2 +(m-MID)*spaces + 0.5*spaces,i*2)
            P.draw(win)
            
    old_pasc = new_pasc
    new_pasc = []
win.getMouse()
win.close()
done()