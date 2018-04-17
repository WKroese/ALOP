# Latest update: 17-04-2018
# File to plot the collected data
# Daphne Abbink, Willem Kroese, Sacha van Ruiten, Yke Rusticus, Kira Strelow

import numpy as np
import matplotlib.pyplot as plt

# This will become code to read in all saved data points and plot them.
t, m_V, err_m_V, m_R, err_m_R = np.loadtxt('datapoints.txt', delimiter='\t', unpack=True)

def colour():
    VR = m_V - m_R
    err_VR = np.sqrt(err_m_V**2 + err_m_R**2)
    return(VR, err_VR)

def plot_V():
    
    return()

def plot_R():
    return()

def plot_col():
    return()


VR_colour, err_col = colour()                  
