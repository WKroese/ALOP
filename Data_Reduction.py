# Latest update: 17-04-2018
# Data reduction code for ALOP
# Daphne Abbink, Willem Kroese, Sacha van Ruiten, Yke Rusticus & Kira Strelow

import numpy as np
import astropy.io as ast
from astropy.io import fits
import matplotlib.pyplot as plt
import sp

# Image = (source + sky)*flat + bias

def import_data():
    filename = raw_input("Enter filename")   
    hdul = ast.open(filename+".fits") 
    im1 = hdul[1].data 
    hdr1 = hdul[1].header 
    hdul.close()
    return()

def files():
    Vfile = raw_input('Enter filename V-exposure\n')
    Rfile = raw_input('Enter filename R-exposure\n')
    Vbias = raw_input('Enter filename V-bias-exposure\n')
    Rbias = raw_input('Enter filename R-bias-exposure\n')
    Vflat = raw_input('Enter filename V-flatfield-exposure\n')
    Rflat = raw_input('Enter filename R-flatfield-exposure\n')

    image_V = fits.getdata(Vfile)
    image_R = fits.getdata(Rfile)
    bias_V = fits.getdata(Vbias)
    bias_R = fits.getdata(Rbias)
    flat_V = fits.getdata(Vflat)
    flat_R = fits.getdata(Rflat)

    exp_t_image_V = ...
    exp_t_image_R = ...
    exp_t_flat_V = ...
    exp_t_flat_R = ...
    return(image_V, image_R, bias_V, bias_R, flat_V, flat_R, exp_t_image_V, exp_t_image_R, exp_t_flat_V, exp_t_flat_R)

def callib():
    image_V -= bias_V
    image_R -= bias_R
    normflat_V = flat_V/np.mean(flat_V)
    normflat_R = flat_R/np.mean(flat_R)
    image_V = image_V/(normflat_V/exp_t_flat_V*exp_t_image_V)
    image_R = image_R/(normflat_R/exp_t_flat_R*exp_t_image_R)

    #hmin is minimal threshold for detection. Should be 3-4 sigma above background RMS
    [xR,yR,fluxR,sharpnessR,roundnessR] = sp.find(image_R,hmin ,5. )
    [xV,yV,fluxV,sharpnessV,roundnessV] = sp.find(image_V,hmin ,5. )

    # Bij skyrad even zelf invullen: Two element vector giving the inner and outer radii to be used for the sky annulus
    [fluxR, fluxRerr, skyR, skyerrR] = sp.aper(image=image_R, xc=xR, yc=yR, phpadu=5., apr=[5], skyrad=[...,...], badpix=[0,0], flux=True,nan=True)
    [fluxV, fluxVerr, skyV, skyerrV] = sp.aper(image=image_V, xc=xV, yc=yRV phpadu=5., apr=[5], skyrad=[...,...], badpix=[0,0], flux=True,nan=True)
    return()




    
#def select_star(): 
#    #Selecteer ster met DS9
#   
#    return pass
#
#def data_reduction():
#    
#    data = import_data()
    
    
    
    
    
    
