suma = 0
num = int(input("ingrese un numero "))
for i in range(0, num+1):
    if i % 2 == 1:
        suma += i

print(f"la suma de todos los numeros impares entre 0 y {num} es de {suma}")
input("")
# En este codigo el usuario ingresa un numero el que entra en un ciclo "for", el cual recorre todos los numeros, desde 0
# hasta el numero ingresado mas uno (num), y utilizando el operador modulo comprueba si el numero es par o impar, si este es
# impar sera sumado en la variable suma, luego de terminar el ciclo imprime la suma total de los impares.
