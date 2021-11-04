from matplotlib.pyplot import xlabel
import numpy as np
import scipy.integrate as spi
f""""
Group 6
Nadya Cindy Putri / 12320019
Ahmad Muchamad Zainulwafa / 12320020
Iqram Haris Fahromi / 12320021
"""
a = 0
b = 1
n = 10
def f(x):
    return np.sqrt(x) #

def penyelesaian(x0, xn, n):
    h = (xn - x0) / n
    
    hasil = f(x0) + f(xn)
    
    for i in range(1,n ):
        k = x0 + i*h
        
        if i%2 == 0:
            hasil = hasil + 2 * f(k)
        else:
            hasil = hasil + 4 * f(k)
    
    hasil = hasil * h/3
    
    return hasil

jawaban = penyelesaian(a, b, n)
print('simpson numerik =', jawaban)

## analitik gauss
x = np.linspace(a,b,n+1)
analitik_gauss = spi.simpson(np.sqrt(x), x)

print('simpson analitik =', analitik_gauss)
print('galat =', abs(analitik_gauss-jawaban))
