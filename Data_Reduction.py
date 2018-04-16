#Data reduction code for ALOP 16/04/2018
#Daphne Abbink, Willem Kroese,Sacha van Ruiten, Yke Rusticus, Kira Strelow

import numpy as np
import astropy.io as ast
import matplotlib.pyplot as plt

def import_data():
    filename = raw_input("Enter filename")
    
    hdul = ast.open(filename+".fits") 
    im1 = hdul[1].data 
    hdr1 = hdul[1].header 
    hdul.close()
    
    
    return 


    
def select_star(): 
    #Selecteer ster met DS9
   
    return pass

def data_reduction():
    
    data = import_data()
    
    
    
    
    
    
