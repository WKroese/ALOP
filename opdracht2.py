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

# Opdracht2
def load():
    
    data = np.loadtxt('51Peg mayorqueloz95.dat', dtype = str,unpack=True, skiprows=0)
    
    return data
    
print load()
