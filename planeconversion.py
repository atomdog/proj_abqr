import numpy as np

def planeconversion(x,y,d,maG,maL):
    x0 = x
    y0 = y
    xcomb = 1
    theta = (maG + (maL-90)) % 360
    qel=[(theta/90), (theta/180), (theta/270), (theta/360)]
    quadrant = 1+np.argmin(qel)
    thetastored = theta
    theta = np.radians(theta)
    if(quadrant==2 or quadrant==3):
        xcomb = -1
    yadd = d * (np.sin(theta))
    xadd = np.sqrt((d**2) - (yadd**2))
    xadd*=xcomb
    x+=xadd
    y+=yadd
    print("Scanned point:("+str(x0)+","+str(y0)+") by "+str(d)+" units to " + str(thetastored) + " degrees: ("+str(x)+","+str(y)+")")
    return(x,y)
points=planeconversion(0,0,10,278,90)
#for x in range(0, 361):
#    planeconversion(0,0,10,x,90)

    