import numpy as np
import matplotlib.pyplot as plt
f""""
Group 6
Nadya Cindy Putri / 12320019
Ahmad Muchamad Zainulwafa / 12320020
Iqram Haris Fahromi / 12320021
"""
#### Trapezoidal Rule
print('Trapezoidal Rule'.center(50, '='))
t = [1, 2, 3.25, 4.5, 6, 7, 8, 9, 9.5, 10]
v = [5, 6, 5.5, 7, 8.5, 8, 6, 7, 7, 5]

print(f't(min) : {t}')
print(f'v(m/s) : {v}')
print('')

ans = 0
temp = 0
for i in range(len(t)-1):
    print(f'I({i})', '=', '(', t[i+1], '-', t[i],')', '*', '((', v[i], '+', v[i+1],')/2)','=', (t[i+1] - t[i])*((v[i]+v[i+1])/2))
    ans = ans + (t[i+1] - t[i])*((v[i]+v[i+1])/2)

print('total =', ans)
ans = ans*60
print('')
print('answer =', ans)


#### Grafik
plt.scatter(t, v, c = "red", alpha=0.5, marker = 'd', label = 'v (m/s)')
plt.ylabel('Velocity (m/s)', color = 'blue')
plt.xlabel('Time (min)', color = 'blue')

### trendline
koeff = np.polyfit(t, v, 2)
t_trend = np.linspace(t[0], t[-1], 1000)
v_trend = np.polyval(koeff, t_trend)

plt.plot(t_trend, v_trend, label = 'poly. (v)')
plt.legend(loc = 4)
plt.xlim(0, 11)
plt.ylim(0, 9)
plt.grid(c = 'blue', alpha = 0.2)

plt.show()

