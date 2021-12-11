import sympy as sym
import numpy as np

x = sym.Symbol('x')

d1 = sym.diff(sym.exp(-2*x) + x**2 - 1)
d2 = sym.diff(d1)

print(d1)
print(d2)

sym.plot(d1, d2, (x, 0, 10), ylabel='Speed')




def bisection(func, a, b, tolerance, maxIterations, counter):
    middle = (a + b) / 2
    counter += 1


    if maxIterations == counter:
        print("Max iterations")
        return middle, counter
    else:
        #print(np.abs(func(middle)))
        #print(tolerance)
        if func(middle) == 0 or np.abs(func(middle)) < tolerance:
            return middle, counter
        else:
            if func(middle) < 0:
                return bisection(func, middle, b, tolerance, maxIterations - 1, counter)
            elif func(middle) > 0:
                return bisection(func, a, middle, tolerance, maxIterations - 1, counter)

def secant(func, a, b, tolerance, maxIterations, counter):
    if func(a) * func(b) >= 0:
        print("f(a) * f(b) >= 0")
        return
    else:
        counter += 1
        #pierwiastek z funkcji liniowej(siecznej)
        x = b - (func(b) * ((b - a) / (func(b) - func(a))))

        if maxIterations == counter:
            return x, counter

        elif func(x) == 0 or np.abs(func(x)) < tolerance:
            return x, counter

        elif func(a) * func(x) < 0:
            return secant(func, a, x, tolerance, maxIterations, counter)
        else:
            return secant(func, x, b, tolerance, maxIterations, counter)

def brents(f, a, b, tolerance, maxIterations, counter):
    if f(a) * f(b) >= 0:
        print("f(a) * f(b) >= 0")
        return
    if np.abs(f(a)) < np.abs(f(b)):
        a, b = b, a

    c = a
    d = 0
    flag = True
    while counter < maxIterations and np.abs(b - a) > tolerance:
        #if f(x) == 0 or np.abs(f(x)) < tolerance or f(x) == 0:
            #return x, counter
        if f(a) != f(c) and f(c) != f(b):                               #}
            x1 = (a * f(b) * f(c)) / ((f(a) - f(b)) * (f(a) - f(c)))    #}
            x2 = (b * f(a) * f(c)) / ((f(b) - f(a)) * (f(b) - f(c)))    #} odwrotna interpolacja kwadratowa
            x3 = (c * f(a) * f(b)) / ((f(c) - f(a)) * (f(c) - f(b)))    #}
            x = x1 + x2 + x3                                            #}
        else:
            x = b - (f(b) * ((b - a) / (f(b) - f(a))))                  # metoda siecznych
        if (x < ((3 * a + b) / 4) or (x > b)) or (flag and np.abs(x - b) >= (np.abs(b - c)/2)) or (not flag and np.abs(x - b) >= (np.abs(c - d)/2)) or (flag and np.abs(b - c) < (np.abs(tolerance))) or (not flag and np.abs(c - d) >= np.abs(tolerance)):
            x = (a + b) / 2                                             #}metoda bisekcji
            flag = True                                                 #}
        else:
            flag = False

        d, c = c, b

        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
        if np.abs(f(a)) < np.abs(f(b)):
            a, b = b, a

        counter += 1
    return x, counter



f = lambda x: x**3 - x - 2
a = 1
b = 2

print("Bisekcja:")
print(bisection(f, a, b, 0.01, 20, 0))

print("Sieczne:")
print(secant(f, a, b, 0.01, 20, 0))

print("Brenta:")
print(brents(f, a, b, 0.01, 20, 0))


