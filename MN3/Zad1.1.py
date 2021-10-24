from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt

# Przyklady operacji na wielomianach
p = Polynomial([3, 2, 1]) # Od ostatniego współczynnika
print(p)
print(p.roots())
print(Polynomial.roots(p))

p2 = Polynomial.fromroots([i for i in range(1, 16)])
print(p2.coef)
print(p2.roots())
p2.coef[13] += pow(1/10, 5)
print(p2.coef)
print(p2.roots())

x = [i.real for i in p2.roots()]
y = [i.imag for i in p2.roots()]

plt.scatter(x, y)
plt.ylabel("Imaginary")
plt.xlabel("Real")
plt.show()