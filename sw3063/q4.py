import numpy as np
import operator


N_max = 50
some_threshold = 50

m = 5 + 1j*3
m
m.imag
m.real
m.conjugate
m.conjugate()
abs(m)

n = 1000
N = 1000
x = np.linspace(-2,1,N)
y = np.linspace(-1.5,1.5,N)
x
y
c = []
for i in range(N):
    for k in range(N):
        c.append(x[i] + 1j*y[k])
N = 100
x = np.linspace(-2,1,N)
y = np.linspace(-1.5,1.5,N)
for i in range(N):
    for k in range(N):
        c.append(x[i] + 1j*y[k])
c = []
for i in range(N):
    for k in range(N):
        c.append(x[i] + 1j*y[k])
c
c[-1]
type(c)
c[0]
N_max = 50
some_threshold = 50
z = c
for v in range(N_max):
    z = operator.pow(z, 2) + c
c = np.array(c)
for v in range(N_max):
    z = operator.pow(z, 2) + c
z = c
for v in range(N_max):
    z = operator.pow(z, 2) + c
z
c
c[0]



import matplotlib.pyplot as plt 
plt.imshow(mask.T, extent= [-2, 1, -1.5, 1.5])
plt.gray()
plt.savefig('mandelbrot.png')

for v in range(N_max):
    z = operator.pow(z, 2) + c
    abs(z) < some_threshold
for v in range(N_max):
    z = operator.pow(z, 2) + c
    if abs(z) < some_threshold:
        break