import numpy as np
import math


k = 1240 * np.sqrt(7)
m = 2048
l = 2j
d = k + 2*m
c = d + l

print(k)
print(type(k))
print(m)
print(type(m))
print(l)
print(type(l))
print(d)
print(type(d))
print(c)
print(type(c))

tab = np.array([1,2,3])
tab2 = np.array(([1.0,2],[3,4])) # argument w postaci krotki!
print(f'{tab}, typ: {type(tab)}')
print(f'{tab2}, typ: {type(tab2)}')

def printDetails(arr):
    print(f'Tablica {arr}')
    print(f'   shape = {arr.shape}')
    print(f'   size = {arr.size}')
    print(f'   ndim = {arr.ndim}')
    print(f'   nbytes = {arr.nbytes}')
    print(f'   dtype = {arr.dtype}')
    print()

printDetails(tab) # Uwaga na shape!
printDetails(tab2)

tab3 = tab.reshape(1,3)
printDetails(tab3)

#tab4 = tab.reshape(10,3)

zeros = np.zeros((2,2))
print(zeros)

ones = np.ones([5,10])
print(ones)

iden = np.identity(10)
print(iden)

eye = np.eye(10)
print(eye)

linspace  = np.linspace(1,5,10)
print(linspace)
