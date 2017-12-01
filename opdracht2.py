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
    
    f= 0#
    
    v_R = k * np.sin(2*np.pi*(f+f_0)) +v_0   
    
    X_2 = 
    
    

def plot():
    
    data = load()
    
    plt.scatter(data[0],data[1])
    plt.xlabel('date')
    plt.ylabel('radial velocity')
    plt.show()

plot()
