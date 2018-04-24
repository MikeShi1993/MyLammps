import numpy as np


def angle_Pn(filename):
    data = np.loadtxt(filename, skiprows=1)
    header = 'Angle Pn'
    np.savetxt(filename, data, header=header, comments='')


def ring_Pn(filename):
    data = np.loadtxt(filename, skiprows=1)
    header = '#ring Pn'
    np.savetxt(filename, data, header=header, comments='')
