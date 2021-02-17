import numpy as np

def calc_alpha(n):
    if n == 2:
        alpha = 1/np.sqrt(2)
    else:
        alpha = np.sqrt((1+calc_alpha(n-1))/2)
    return alpha

k = int(input("¿Cuántas iteraciones quiere hacer? \n"))

SUMA = 1

for i in range(2,k+1):
    a = calc_alpha(i)
    SUMA *= a

pi = 2 / SUMA

print(f"π = {pi}")