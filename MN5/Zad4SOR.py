import numpy as np
import matplotlib.pyplot as plt


def SOR(A, b, w, tol, maxIT):
    g = np.zeros(b.shape)
    IT = 0

    while True:
        IT += 1
        if IT >= maxIT:
            print("Osiagnieto limit iteracji")
            break
        for i in range(A.shape[0]):
            sigma = 0
            for j in range(A.shape[1]):
                if j != i:
                    sigma += A[i][j] * g[j]
            g[i] = (1 - w) * g[i] + (w / A[i][i]) * (b[i] - sigma)
        n = np.linalg.norm(np.matmul(A, g) - b)
        if n < tol:
            print("Liczba iteracji:", IT)
            break

    return g, IT


A = np.array(
    [[4, -1, -6, 0],
     [-5, -4, 10, 8],
     [0, 9, 4, -2],
     [1, 0, -7, 5]]
)
b = np.array([2, 21, -12, -6])

maxIT = 10000
w = 0.5

print("A=", A)
print("b=", b)
print("Dla omega=", w)
res, IT = SOR(A, b, w, 1e-8, maxIT)
print(res)
print("\n")

A2 = np.array(
    [[3, -1, 1],
     [-1, 3, -1],
     [1, -1, 3]]
)

b2 = np.array([-1, 7, -7])

maxIT = 10000
w = 1.2
print("A=", A2)
print("b=", b2)
print("Dla omega=", w)
res, IT = SOR(A2, b2, w, 1e-8, maxIT)
print(res)
print("\n")

A3 = np.array(
    [[-2, -3, 5],
     [4, 3, -2],
     [1, 1, -1]]
)

b3 = np.array([1, 3, -1])

maxIT = 10000
w = 1.2
print("A=", A3)
print("b=", b3)
print("Dla omega=", w)
res, IT = SOR(A3, b3, w, 1e-8, maxIT)
print(res)
print("\n")

np.seterr(all="raise")


def omegaTest(A, b):
    print("Test dla 0<ω<3")
    print("A =", A)
    print("b =", b)
    spectralRadius = list()
    omega = list()
    ITlist = list()
    for i in range(1, 300):
        w = i * 0.01


        # macierz iteracji
        # zrodlo: https://mst.mimuw.edu.pl/lecture.php?lecture=mo2&part=Ch5#S3.SS3
        # https://mst.mimuw.edu.pl/wyklady/mo2/mi/mi1177.png
        G = (np.tril(A) - np.tril(A, -1)) + (w * np.tril(A, -1))
        G = np.linalg.inv(G)
        H = ((1 - w) * (np.tril(A) - np.tril(A, -1)) - w * np.triu(A, 1))
        G = np.matmul(G, H)
        T = np.linalg.eigvals(G)
        spectralRadius.append(max(abs(T)))
        omega.append(w)

        print("Dla omega =", str(w))
        try:
            res, IT = SOR(A, b, w, 1e-8, maxIT)
            print(res)
            print(IT)
            ITlist.append((w, IT))


        except FloatingPointError:
            print(" nie jest zbiezna")
            print("RunTimeError")
        print("")
    #print(min(list((zip(*ITlist))[1])))

    minIT = min([x[1] for x in ITlist])
    bestW = 0
    for x in ITlist:
        if x[1] == minIT:
            bestW = x[0]
            break
    print("Najmniejsza liczba iteracji:", minIT, "dla omega = ", bestW)

    return spectralRadius, omega


spectralRadius, omega = omegaTest(A3, b3)
plt.plot(omega, spectralRadius)
plt.ylabel("ρ(T)")
plt.xlabel("ω")
plt.title("Zależność promienia spektralnego macierzy iteracji od ω")
plt.ylim([0.4, 1])  # Przedział dla y taki jak na slajdzie z wykładu
plt.show()

#Wniosek: najlepsza omega (1.24) jest widoczna na wykresie, widać analogię
#do przykładu opisanego na wykładzie
