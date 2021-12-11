import numpy as np

A = np.random.rand(3,3)
b = np.random.rand(3)
print(A,b)

def Jacobi(A, b):
    print(A)
    print(b)
    D = np.zeros((3,3))
    print(D)

d = np.diag(A)
print(d)
np.fill_diagonal(D, d)
print(D)
L = np.tril(A)
U = np.triu(A)
x = np.zeros(3)
x = -(np.linalg.inv(D)) @ (L + U) @ x + (np.linalg.inv(D)) @ b
n = 0
while True:
    x = -(np.linalg.inv(D)) @ (L + U) @ x + (np.linalg.inv(D)) @ b
    print(-(np.linalg.inv(D)) @ (L + U) @ x)
    if -(np.linalg.inv(D)) @ (L + U) @ x < 1:
        break
    n+=1
    if n > 10:
        break

def Gauss(A, b):
    D = np.diag(A)
    L = np.tril(A)
    U = np.triu(A)
    while True:
        x = -(np.linalg.inv(L + D)) * U * x + np.linalg.inv(L+D) * b

    Jacobi(A,b)