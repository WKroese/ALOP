
import numpy as np
import astropy.io as ast
from astropy.io import fits
import matplotlib.pyplot as plt
#import sp

# Image = (source + sky)*flat + bias

def import_data(a):
    filename = raw_input("Enter "+a+"-file number\n")   
    hdul = fits.open("r"+filename+".fit") 
    im1 = hdul[1].data 
    hdr1 = hdul[0].header 
    hdul.close()
    
    print hdr1
    return()


def make_cal_im(a,b):
    number1 = int(raw_input("first file number "+a+"\n"))
    number2 = int(raw_input("last file number "+a+"\n"))
    cal_im_total = np.zeros([4200,2154])
    
    for i in range(number1,number2+1,1):
        filename = "r"+str(i)+".fit"
        hdul = fits.open(filename) 
        im = hdul[1].data 
        hdr1 = hdul[1].header 
        hdul.close()
        if b:
            
            im /= np.mean(im)
            #Door met de flat normalisere/integratietijd dingen... zaken... entiteiten...
            
            
        cal_im_total += im
    cal_im = cal_im_total/(float(number2-number1+1))
    
    return cal_im      

def files():
    Vfile = raw_input('Enter filename V-exposure\n')
    Rfile = raw_input('Enter filename R-exposure\n')
    bias = raw_input('Enter filename bias-exposure\n')
    Vflat = raw_input('Enter filename V-flatfield-exposure\n')
    Rflat = raw_input('Enter filename R-flatfield-exposure\n')
    
    
    

    image_V = fits.getdata(Vfile)
    image_R = fits.getdata(Rfile)
    bias = fits.getdata(bias)
    flat_V = fits.getdata(Vflat)
    flat_R = fits.getdata(Rflat)

    exp_t_image_V = 0
    exp_t_image_R = 0
    exp_t_flat_V = 0
    exp_t_flat_R = 0
    return(image_V, image_R, bias, flat_V, flat_R, exp_t_image_V, \
    exp_t_image_R, exp_t_flat_V, exp_t_flat_R)
    
#files()

def callib():
    image_V -= bias
    image_R -= bias
    normflat_V = flat_V/np.mean(flat_V)
    normflat_R = flat_R/np.mean(flat_R)
    image_V = image_V/(normflat_V/exp_t_flat_V*exp_t_image_V)
    image_R = image_R/(normflat_R/exp_t_flat_R*exp_t_image_R)

    #hmin is minimal threshold for detection. Should be 3-4 sigma above background RMS
    [xR,yR,fluxR,sharpnessR,roundnessR] = sp.find(image_R,hmin ,5. )
    [xV,yV,fluxV,sharpnessV,roundnessV] = sp.find(image_V,hmin ,5. )

    # Bij skyrad even zelf invullen: Two element vector giving the inner and outer radii to be used for the sky annulus
    [fluxR, fluxRerr, skyR, skyerrR] = sp.aper(image=image_R, xc=xR, yc=yR, \
    phpadu=5., apr=[5], skyrad=[0,0], badpix=[0,0], flux=True,nan=True)
    [fluxV, fluxVerr, skyV, skyerrV] = sp.aper(image=image_V, xc=xV, yc=yRV, \
    phpadu = 5., apr=[5], skyrad=[0,0], badpix=[0,0], flux=True,nan=True)
    return()
    
    
raw_R = import_data("R")
#raw_V = import_data("V")
bias = make_cal_im("bias",False)
flat_R = make_cal_im("flat_R",True)
flat_V = make_cal_im("flat_V",True)



