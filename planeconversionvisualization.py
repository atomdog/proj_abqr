#planeconversionvisualization
import numpy as np
import Tkinter
import tkMessageBox
import random as rn

def planeconversion(x,y,d,maG,maL):
    xcomb = 1
    ycomb = 1
    theta = (maG + (maL-90)) % 360
    qel=[(theta/90), (theta/180), (theta/270), (theta/360)]
    quadrant = 1+np.argmin(qel)
    thetastored = theta
    theta = np.radians(theta)

    if(quadrant==3 or quadrant==2):
        xcomb = -1
	
    yadd = d * (np.sin(theta))
    xadd = np.sqrt((d**2) - (yadd**2))
    xadd= xadd * xcomb
    yadd= yadd * ycomb
    x+=xadd
    y+=yadd
    print(thetastored)
    print(x,y)
    print("#")
    return(x,y)
#points=planeconversion(250,450,10,90,90)
#for x in range(0, 361):
#    planeconversion(0,0,10,x,90)
top = Tkinter.Tk()

C = Tkinter.Canvas(top, bg="black", height=500, width=500)

for l in range(0,361):
    points=planeconversion(250,250,rn.randint(1,40),l,90)
    coord = points[0]-0.5, points[1]-0.5, points[0]+0.5, points[1]+0.5
    line = C.create_line(coord, fill="white")

C.pack()
top.mainloop()