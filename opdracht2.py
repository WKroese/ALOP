import astropy as ass
import matplotlib.pyplot as plt
import numpy as np
import emcee as emc
import corner as cor

#Opdracht1
G = 6.67408*10**(-11) # m^3/kg*s^2
Mj = 1.898*10**(27) #kg
Mzon = 1.989*10**(30) #kg

def k(P, i, Mp, Mster):
    k = ((2*np.pi*G)/(365.25*P))^(1/3) * (Mp*Mj*np.sin(i)) / (Mp*Mj + Mster*Mzon)**(2/3)
    # P is periode in dagen
    # Mp is massa v/d planeet in jupitermassa's
    # i is inclinatiehoek in graden
    # Mster is massa v/d ster in zonsmassa's
    return k

kEarth = k(365.25, np.pi/2, 1/317.8, 1)
kJupiter = k(4332.71, np.pi/2, 1, 1)
print ("kEarth =", kEarth, "kJupiter =", kJupiter)

# Opdracht2
def load():
    
    data = np.loadtxt('51Peg mayorqueloz95.dat', dtype = str,unpack=True, skiprows=0)
    
    return data
    
print load()

def leastsquares(k,P,f_0,v_0):
    
    data = load()
    t=data[0]
    v = data[1]
    sigma = data[2]
    
    f = 1/P * t
    
    v_model = k * np.sin(2*np.pi*(f+f_0)) +v_0   
    X_2 = 0

    for i in range(len(v)):
        X_2 += ((v[i]-v_model[i])/sigma[i])**2
        
    
    return X_2
    
    

    
def plot():
    
    data = load()
    
    plt.plot(data[0],data[1])
    plt.xlabel('date')
    plt.ylabel('radial velocity')
    
    k=60
    P=4
    
    x=[]

    
    for P in np.linspace(3,5,200):     # Hij maakt nog veel te veel berekeningen. Hoe kunnen we beter k en P bepalen..?
        for k in np.linspace(50,70,200):
            #for f_0 in np.linspace(0,1,100):
            f_0=0.5
            y_least = leastsquares(k,P,f_0,10)
            x.append(y_least)
            
    print x

    plt.show()
    

plot()


HOI WILLY!
