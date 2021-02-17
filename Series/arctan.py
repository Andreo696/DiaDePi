def atan1(n):
    s = 0 # Asigna el valor 0 a la suma
    for i in range(0, n):
        a = (-1)**i / (2*i + 1) # Calcula el valor de cada término en a suma
        s = s+a # Suma cada término al valor s
    return s # Devuelve la suma s
def pi(n):
    return 4 * atan1(n)
print("Hola. Este programa calcula una aproximación de π mediante la serie de Taylor de la arcotangente")
it = int(input("Ingrese cuántos términos de la serie desea sumar: ")) # Pide la cantidad de términos a sumar
print("π =", pi(it)) # Imprime el resultado