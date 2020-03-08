import arraytool.planar as planar
import numpy as np

a = 0.6 # separation between the elements along x-axis (normalized WRS wavelength)
b = 0.5 # separation between the elements along y-axis (normalized WRS wavelength)
M = 10 # no. of elements along x-axis
N = 11 # no. of elements along y-axis

A = np.ones((N, M)) # Uniform planar excitation

# Converting the 'excitation & position' information into Arraytool input format
array_ip = planar.ip_format(a, b, A)

# Calling the 'pattern_tp' function to evaluate and plot 3D AF/GF/NF
[tht, phi, AF] = planar.pattern_tp(array_ip, tht_scan=(0)*np.pi, phi_scan=(0)*np.pi, tht_min= 0,
                  tht_max=0.5*np.pi, tht_num=200, phi_min= 0*np.pi, phi_max=2*np.pi,
                  phi_num=200, scale="dB", dB_limit= -40, factor="GF", plot_type="polar")