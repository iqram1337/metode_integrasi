import numpy as np
import scipy.integrate as spi
f""""
Group 6
Nadya Cindy Putri / 12320019
Ahmad Muchamad Zainulwafa / 12320020
Iqram Haris Fahromi / 12320021
"""
f""""
rumus = ((b-2)/2) * [w1*f(x1) + w2*f(x2)]

"""
##### Gaussian Quadrature
def f(x):
    return np.sqrt(x) #

a = 0
b = 1
w1 = w2 = 1
z1, z2 = -1/(np.sqrt(3)), 1/(np.sqrt(3))

x1 = ((b-a)/2)*z1 + ((b+a)/2)
x2 = ((b-a)/2)*z2 + ((b+a)/2)

gauss_numerik =  ((b-a)/2) * ((w1*f(x1)) + (w2*f(x2)))
print('Gauss numerik =', gauss_numerik)
