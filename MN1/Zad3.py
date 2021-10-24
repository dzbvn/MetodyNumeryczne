import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

X = np.linspace(0,2*np.pi, 10)
Y = np.sin(X)

#plt.plot(X,Y)
#plt.title('Wykres $sin(x)$')
#plt.xlim([0,2*np.pi])
#plt.xlabel('x')
#plt.ylabel('sin(x)')

plt.figure(figsize=(14,10)) # Stworzenie ,,większego'' okna
X = np.linspace(-10,10, 1000)

plt.plot(X,X**2, label = '$x^2$') # W argumencie label umieszcza się nazwy krzywych do legendy
plt.plot(X,X**3, label = '$x^3$')
plt.plot(X,np.tan(X), label = '$tg(x)$')
plt.xlim([-10,10])
plt.ylim([-100,100])
plt.xlabel('x')
plt.grid() # Wyświetlanie siatki
plt.legend() # Dodanie legendy
plt.axhline(y=0, color='k') # Dodanie osi x = 0
plt.axvline(x=0, color='k') # Dodanie osi y = 0

#plt.figure()
#X = np.linspace(0,2*np.pi, 50)
#plt.plot(X,np.sin(X), '*')
#plt.title('Wykres $sin(x)$')
#plt.xlim([0,2*np.pi])
#plt.xlabel('x')
#plt.ylabel('sin(x)')

plt.figure()
X = np.linspace(0,2*np.pi, 50)
plt.plot(X,np.sin(X), 'r+')
plt.title('Wykres $sin(x)$')
plt.xlim([0,2*np.pi])
plt.xlabel('x')
plt.ylabel('sin(x)')

plt.figure()
X = np.linspace(-1, 1, 50)
Y = X**3-5*X+7
plt.plot(X, Y, 'r')
plt.xlabel('x')
plt.ylabel('$x^3$ - $5*x$ + 7')
plt.title('Wykres $x^3$ - $5*x$ + 7 w przedziale <-1,1>')

plt.figure()
X = np.linspace(-10, 20, 50)
Y = X**3-5*X+7
plt.plot(X, Y, 'r*')
plt.xlabel('x')
plt.ylabel('$x^3$ - $5*x$ + 7')
plt.title('Wykres $x^3$ - $5*x$ + 7 w przedziale <-10,20>')

plt.show()
