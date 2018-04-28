import numpy as np
import astropy.io as ast
from astropy.io import fits
import matplotlib.pyplot as plt

np.loadtxt


def open_file():
    for filename in filenames:
        hdul = fits.open(filename) 
        im = hdul[4].data 
        hdr0 = hdul[0].header 
        hdul.close()
        return im
