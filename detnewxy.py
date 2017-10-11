import numpy as np

def detnewxy(x,y,d,maG):
    xcomb = 1
    theta = maG
    qel=[(theta/90), (theta/180), (theta/270), (theta/360)]
    quadrant = 1+np.argmin(qel)
    thetastored = theta
    theta = np.radians(theta)
    if(quadrant==2|quadrant==3):
        xcomb = -1
    yadd = d * (np.sin(theta))
    xadd = np.sqrt((d**2) - (yadd**2))
    xadd*=xcomb
    x+=xadd
    y+=yadd
    print(thetastored)
    print(x,y)
    print("#")
    return(x,y)
points=detnewxy(5,5,10,45)
