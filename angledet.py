import numpy as np

def angledet(xc,yc,xf,yf):
    d = np.sqrt(((xf-xc)**2) + ((yf-yc)**2))
    theta = np.arcsin((yf-yc)/d)
    theta = np.degrees(theta)
    cxf = xf
    cyf = yf

    if(cxf < 0 and cyf < 0):
        theta = 180-theta

    elif(cxf < 0 and cyf >= 0):
        theta = 270-theta
        
    elif(cxf >= 0 and cyf < 0):
        theta = 360+theta


    print("Distance:("+str(xc)+","+str(yc)+")->("+str(xf)+","+str(yf)+"): " + str(d))
    print("Angle:("+str(xc)+","+str(yc)+")->("+str(xf)+","+str(yf)+"): " + str(theta))
    return(theta)
angledet(0,0,1.3917310096,-9.90268068742)
    