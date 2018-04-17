#Data reduction code for ALOP 16/04/2018
#Daphne Abbink, Willem Kroese,Sacha van Ruiten, Yke Rusticus, Kira Strelow

import numpy as np
import astropy.io as ast
from astropy.io import fits
import matplotlib.pyplot as plt
import sp

##Image = (source + sky)*flat + bias
#def import_data():
#    filename = raw_input("Enter filename")
#    
#    hdul = ast.open(filename+".fits") 
#    im1 = hdul[1].data 
#    hdr1 = hdul[1].header 
#    hdul.close()
#    return()
#
#path = "Enter path name"
## Als er meerdere bias opnames zijn: allemaal importeren, bij elkaar optellen en delen door het aantal
#bias = fits.open(path+"Enter bias file name")
#Exptimebias = 
#
## Per filter doen
#sky = fits.open(path+"Enter sky file name")
#Exptimesky =
#
#flatR = fits.open(path+"Enter flat R-filter file name")
#ExptimeflatR =
#flatV = fits.open(path+"Enter flat V-filter file name")
#ExptimeflatV =
#
#NormflatR = flatR/ExptimeflatR
#NormflatV = flatV/ExptimeflatV
#
## Verkregen data van telescoop - bias
## Devide by normalised flat
## Calibrate image
#
#Source = (im1 - bias)/normflat - sky# R or V, depending on in which filter the image is


image_R = fits.getdata("Enter file name Rfilter exposure")
image_V = fits.getdata("Enter file name Vfilter exposure")

#hmin is minimal threshold for detection. Should be 3-4 sigma above background RMS
[xR,yR,fluxR,sharpnessR,roundnessR] = sp.find(image_R,hmin ,5. )
[xV,yV,fluxV,sharpnessV,roundnessV] = sp.find(image_V,hmin ,5. )

# Bij skyrad even zelf invullen: Two element vector giving the inner and outer radii to be used for the sky annulus
[fluxR, fluxRerr, skyR, skyerrR] = sp.aper(image=image_R, xc=xR, yc=yR, phpadu=5., apr=[5], skyrad=[...,...], badpix=[0,0], flux=True,nan=True)
[fluxV, fluxVerr, skyV, skyerrV] = sp.aper(image=image_V, xc=xV, yc=yRV phpadu=5., apr=[5], skyrad=[...,...], badpix=[0,0], flux=True,nan=True)





    
#def select_star(): 
#    #Selecteer ster met DS9
#   
#    return pass
#
#def data_reduction():
#    
#    data = import_data()
    
    
    
    
    
    
