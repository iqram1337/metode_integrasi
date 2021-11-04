import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi
f""""
Group 6
Nadya Cindy Putri / 12320019
Ahmad Muchamad Zainulwafa / 12320020
Iqram Haris Fahromi / 12320021
"""
#### Trapezoidal Rule
f = lambda x : np.sqrt(x)               #
a = 0
b = 1 
n = 10

x = np.linspace(a,b,n+1)
y = f(x)

trapz_numerik = 0
for i in range(len(x)-1):
    trapz_numerik +=0.5*((x[i+1]) - x[i]) * (y[i+1] + y[i])
print('Trapz numerik =', trapz_numerik)

trapz_analitik = spi.trapz(y, x)
print('Trapz analitik  =', trapz_analitik)


#### Grafik
sumbu_x = np.linspace(a,b,100)
sumbu_y = f(sumbu_x)
plt.plot(sumbu_x, sumbu_y, label = r'$\int_0^1 \sqrt{x} \mathit{dx}$')

for i in range(n):
    xx = [x[i], x[i], x[i+1], x[i+1]]
    yy = [0, f(x[i]), f(x[i+1]), 0]

    plt.fill(xx, yy, 'b', edgecolor = 'r', alpha = 0.2)


plt.title(f'Trapezoidal Rule Graph, N = {n}')

print('galat =', abs(trapz_analitik-trapz_numerik))
plt.legend()
plt.show()