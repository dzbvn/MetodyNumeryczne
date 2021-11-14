import scipy.linalg
import numpy as np

#Macierz Hilberta
hil = scipy.linalg.hilbert(4)

#Macierz Vandermonde'a
x = np.array([1,2,3,4])
van = np.vander(x, increasing=True)

#Losowa macierz z przedziału [0,1]
ran = np.random.rand(4,4)

print(hil)
print("Norma 1, kolumnowa:", np.linalg.norm(hil, 1))
print("Norma 2, spektralna:", np.linalg.norm(hil, 2))
print("Norma inf, wierszowa:", np.linalg.norm(hil, np.inf))
print("Wskaznik uwarunkowania macierzy:", np.linalg.cond(hil))

print(van)
print("Norma 1, kolumnowa:", np.linalg.norm(van, 1))
print("Norma 2, spektralna:", np.linalg.norm(van, 2))
print("Norma inf, wierszowa:", np.linalg.norm(van, np.inf))
print("Wskaznik uwarunkowania macierzy:", np.linalg.cond(van))

print(ran)
print("Norma 1, kolumnowa:", np.linalg.norm(ran, 1))
print("Norma 2, spektralna:", np.linalg.norm(ran, 2))
print("Norma inf, wierszowa:", np.linalg.norm(ran, np.inf))
print("Wskaznik uwarunkowania macierzy:", np.linalg.cond(ran))

'''
for i in range(5,20):
    # Macierz Hilberta
    hil = scipy.linalg.hilbert(i)

    # Macierz Vandermonde'a
    x = np.array([j for j in range(i)])
    van = np.vander(x, increasing=True)

    # Losowa macierz z przedziału [0,1]
    ran = np.random.rand(i, i)
    print(hil)
    print("Norma 1, kolumnowa:", np.linalg.norm(hil, 1))
    print("Norma 2, spektralna:", np.linalg.norm(hil, 2))
    print("Norma inf, wierszowa:", np.linalg.norm(hil, np.inf))

    print(van)
    print("Norma 1, kolumnowa:", np.linalg.norm(van, 1))
    print("Norma 2, spektralna:", np.linalg.norm(van, 2))
    print("Norma inf, wierszowa:", np.linalg.norm(van, np.inf))

    print(ran)
    print("Norma 1, kolumnowa:", np.linalg.norm(ran, 1))
    print("Norma 2, spektralna:", np.linalg.norm(ran, 2))
    print("Norma inf, wierszowa:", np.linalg.norm(ran, np.inf))
'''
