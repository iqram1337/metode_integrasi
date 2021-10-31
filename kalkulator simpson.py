from math import *
##punya gilang
fungsi = input('input math function: ')
f = lambda x: eval(fungsi)
bb = float(input('batas bawah: '))
ba = float(input('batas atas: '))
iterasi = float(input('banyak iterasi: '))
deltaX = (ba-bb)/iterasi
fa = 0
ft = 0
i = bb
while i <= ba:
    fa += f(i)
    ft += f(i+deltaX)
    i += deltaX*2
y = ((2*fa - (f(bb) + f(ba))) + (ft-f(ba+deltaX))*4)*deltaX/3 # rumus integral Simpson setelah disederhanakan
print("Hasil integral simpson: ", y)
