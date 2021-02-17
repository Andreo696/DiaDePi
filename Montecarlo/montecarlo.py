import random
def montecarlo(number):
    n = 0
    for i in range(1,number+1):
        x_i = random.uniform(-1,1)
        y_i = random.uniform(-1,1)
        if x_i**2+y_i**2 <= 1:
            n += 1
    return n
def divi(number):
    c = montecarlo(number)
    d = 4*c / number
    return d
print("Hola. Este programa calcula una aproximación de π mediante el método de Montecarlo.")
k = int(input("Ingrese la cantidad de dardos que quiere lanzar: "))
print("π =",divi(k))