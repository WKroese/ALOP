import astropy as ass
import matplotlib.pyplot as plt
import numpy as np
import emcee as emc
import corner as cor

#Opdracht1


# Opdracht2
def load():
    
    data = np.loadtxt('51Peg mayorqueloz95.dat', dtype = str,unpack=True, skiprows=0)
    
    return data
    
print load()
