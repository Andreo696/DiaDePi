import matplotlib.pyplot as plt
import numpy as np
import random

plt.grid(linestyle='--') # Cuadrícula
plt.xlim(-1.25,1.25) # Límites
plt.ylim(-1.25,1.25)

plt.gca().set_aspect('equal', adjustable='box') # Ejes

ver_x= [1,1,-1,-1,1] # Cuadrado
ver_y= [1,-1,-1,1,1]
plt.plot(ver_x, ver_y)

theta = np.linspace(0, 2*np.pi, 100) # Circunferencia
xc = np.cos(theta)
yc = np.sin(theta)
plt.plot(xc,yc)



plt.title("Método de Montecarlo para aproximar π")

def montecarlo(number):
    n = 0
    for i in range(1,number+1):
        x_i = random.uniform(-1,1)
        y_i = random.uniform(-1,1)
        if x_i**2+y_i**2 <= 1:
            n += 1
        plt.plot(x_i, y_i, '.', color='black') # Puntos
    return n
def divi(number):
    c = montecarlo(number)
    d = 4*c / number
    return d

print("Hola. Este programa calcula una aproximación de π mediante el método de Montecarlo.")
k = int(input("Ingrese la cantidad de dardos que quiere lanzar: "))
print("π =",divi(k))
plt.show()