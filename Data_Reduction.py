# Last update: 17-04-2018
# ALOP La Palma project 'Transients' Data calibration
# Authors: Daphne Abbink, Willem Kroese, Sacha van Ruiten, Yke Rusticus, Kira Strelow

import numpy as np
import astropy.io as ast
from astropy.io import fits
import matplotlib.pyplot as plt
import os
#import sp

# Importeer uit de map waar de data in staat, alle namen van de datafiles
# Naderhand kunnen we een forloop maken en die voor alle bestanden dan in 1 keer laten runnen, in plaats van alles steeds handmatig te importeren
datafiles = os.listdir()

# Function to unpack the data
# 'a' is the filter colour.
def import_data(a):
    filename = raw_input("Enter "+a+"-file number\n")   
    hdul = fits.open("r"+filename+".fit") 
    im = hdul[4].data 
    hdr0 = hdul[0].header 
    hdul.close()
    exp_t = hdr0['EXPTIME']
    return(im, exp_t)

# Function to give the mean bias image or mean normalized flat field image (calibration image).
# parameters: a is either 'bias' or 'flat', depending on the file type.
#             b is 'True' for flats, and 'False' for biases.
def make_cal_im(a,b):
    number1 = int(raw_input("first file number "+a+"\n"))
    number2 = int(raw_input("last file number "+a+"\n"))
    cal_im_total = np.zeros([4200,2154]) # voor ons is dit straks ([1000,1000])
    
    for i in range(number1,number2+1,1):
        filename = "r"+str(i)+".fit"
        hdul = fits.open(filename) 
        im = hdul[1].data 
        hdr0 = hdul[0].header 
        hdul.close()
        if b:
            im /= hdr0['EXPTIME']
        cal_im_total += im
    cal_im = cal_im_total/(float(number2-number1+1))
    if b:
        im /= np.mean(im)
    
    return cal_im

# Thir function calibrates the image with use of:  Image = (source + sky)*flat + bias
# The bias is needed, as well as the exposure time of the image, and the normalized flat field in
# the right filter that has already been devided by the exposure time of th eflat field.
def calibrate(im, im_t, bias, flat):
    im -= bias
    im = image/(flat*im_t)

    #hmin is minimal threshold for detection. Should be 3-4 sigma above background RMS
    [x,y,flux,sharpness,roundness] = sp.find(im,hmin ,5. )

    # Bij skyrad even zelf invullen: Two element vector giving the inner and outer radii to be used 
    # for the sky annulus
    [flux, fluxerr, sky, skyerr] = sp.aper(image=im, xc=x, yc=y, phpadu=5., apr=[5], skyrad=[0,0], \
    badpix=[0,0], flux=True,nan=True)
    return(flux, fluxerr)


''' !!!Hiertussen moeten we eigenlijk kijken welke sterren bruikbaar zijn en welke indices daarbij
horen. Ook de index van de transient moeten we weten, plus de magnitdes van de hulpsterren.!!! '''

# PHOTOMETRIC CALIBRATION

def magnitude(flux, err_flux, m_ref, err_m_ref):
    m_arr = -2.5 * np.log10(flux[0] / flux[1:]) + m_ref # voor de indices nam ik nu even aan dat de 
    err_m_arr = np.sqrt((2.5/(flux[0]*np.log(10))*err_flux[0])**2 + \ # transient op 0 zit, de rest
    ((2.5/(flux[1:]*np.log(10))*err_flux[1:])**2 + err_m_ref**2)      # is dus reference stars.
    m = np.sum(m_arr/(err_m_arr)**2) # take the weighted average of all reference stars
    err_m = np.sum(1./(err_m_ar)**2)
    return(m, err_m)

    
raw_R, t_R = import_data("R")
raw_V, t_V = import_data("V")
bias = make_cal_im("bias",False)
flat_R = make_cal_im("flat_R",True)
flat_V = make_cal_im("flat_V",True)
science_R, err_R = calibrate(raw_R, t_R, bias, flat_R)
science_V, err_V = calibrate(raw_V, t_V, bias, flat_V)
#m_R, err_m_R = magnitude(science_R, err_R, m_R_ref, err_m_R_ref)
#m_V, err_m_V = magnitude(science_V, err_V, m_V_ref, err_m_V_ref)


#OHJA, WE HEBBEN OOK DE JULIAN DATE NODIG NATUURLIJK
# We can use this to add new lines to an existing text file (adding new data points)
#with open('datapoints.txt', 'a') as file:
#    file.writelines('{}\t{}\t{}\t{}\t{}\n'.format(t, m_V, err_m_V, m_R, err_m_R))
