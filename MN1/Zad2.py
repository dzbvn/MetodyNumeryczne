import numpy as np


A = np.array(([1,2,3],[4,5,6],[7,8,9]))
print(A)

print(A[1,1])
print(A[0,0])
print(A[0:2,0:1])
print(A[-1,-1])
print(A[A>5])
print(A[A%2==0])
B = A
B[B>5] = 37
print(B)

A = np.array(([1,2,3],[4,5,6],[7,8,9],[10,11,12]))
B = np.array(([-1,-2,-3],[-4,-5,-6],[-7,-8,-9],[-10,-11,-12]))
C = np.array(([20,21,22,23],[24,25,26,27],[28,29,30,31]))

print(A)
print(B)
print(C)
print(A+B)
print(A-B)
print(B-A)
print(A*B)
print(A/B)
print(np.dot(A,C))
print(A@C)
print(A.T)

M = np.array(([np.sqrt(2), 1, -np.sqrt(2)], [0, 1, 1], [-np.sqrt(2), np.sqrt(2), 1]))
print(M)
print(np.linalg.inv(M))
print(M.T)
print(np.linalg.det(M))
