import numpy as np
import matplotlib.pyplot as plt

v = [5, 6, 5.5, 7, 8.5, 8, 6, 7, 7, 5]
t = [1, 2, 3.25, 4.5, 6, 7, 8, 9, 9.5, 10]

jawaban = 0

for i in range(len(v)-1):
    jawaban = jawaban + (t[i+1]-t[i])*((v[i]+v[i+1])/2)

print(jawaban*60, 'm')

plt.scatter(t, v)
plt.show()
