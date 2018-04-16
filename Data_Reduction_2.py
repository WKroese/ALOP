# 16-04-2018
# Second file for data reduction code
# Daphne Abbink, Willem Kroese, Sacha van Ruiten, Yke Rusticus, Kira Strelow

import numpy as np
import astropy as ast
import matplotlib.pyplot as plt
import csv

# The arrays will contain the transient as well as some other stars, of which 10 to 20 will be used as reference stars
V_Flux = # ...array
R_Flux = # ...array
err_V_Flux = # ...array
err_R_Flux = # ...array

V_m_ref = # This is also an array, since we will use 10 to 20 reference stars
R_m_ref = 
err_V_m_ref = 
err_R_m_ref = 

V_m = -2.5 * np.log10(V_Flux / V_Flux[...]) + V_m_ref # V_Flux[...] --> values that correspond with reference stars
R_m = -2.5 * np.log10(R_Flux / R_Flux[...]) + R_m_ref

# X_Flux[...] is the target and the other one is the array of reference stars
err_V_m = np.sqrt((2.5/(V_Flux[...]*np.log(10))*err_V_Flux[...])**2 + ((2.5/(V_Flux[...]*np.log(10))*err_V_Flux[...])**2 + err_V_m_ref**2)
err_R_m = np.sqrt((2.5/(R_Flux[...]*np.log(10))*err_R_Flux[...])**2 + ((2.5/(R_Flux[...]*np.log(10))*err_R_Flux[...])**2 + err_R_m_ref**2)
# .... gewogen gemiddelde
                  
# We can use this to add new lines to an existing text file (adding new data points)
#with open('file.txt', 'a') as file:
#    file.writelines(V_m, '  ', err_V_m, '  ', R_m, '  ', err_R_m)

# This will become code to read in all saved data points and plot them.         
#with open("tab-separated-values") as tsv:
#    for line in csv.reader(tsv, dialect="excel-tab"): #You can also use delimiter="\t" rather than giving a dialect.
#        ... 
