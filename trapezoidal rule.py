import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 1

def trapz(fa, fb, a, b):
    ans = (b-a)*((fa+fb)/2)
    return ans


def trapezoidal(x):
    fx = 1/(1+x)                     # YG DIUBAH
    return fx


ans = trapz(trapezoidal(a), trapezoidal(b), a, b)
print(ans)

## grafik
x = np.linspace(-0.5, 1.5, 100)
f = lambda x: 1/(1+x)               # YG DIUBAH
y = f(x)
ya = 1/(1+a)                        # YG DIUBAH
yb = 1/(1+b)                        # YG DIUBAH

plt.plot(x, y)
plt.fill_between([a, b], [ya, yb],alpha=0.2, label = 'daerah trapezoid')
plt.xlim([-0.5, 1.5])
plt.ylim([0, 2.5])

plt.legend()
plt.show()