import turtle as tur
lvl = 3
l = 650 

import turtle as tur
tur.speed(10)
tur.ht()
tur.pu()
tur.setpos(-330,0)
tur.pd()

def koch_snowflake(l, lvl):
    """Drawing koch snowflake Recursive Algorithm
    l = length of first level
    lvl = level
    """

    if lvl > 0:
        for t in [60, -120, 60, 0]:
            koch_snowflake(l/3, lvl-1)
            tur.left(t)
    else:
        tur.forward(l)

koch_snowflake(l,lvl)
tur.done()