"""
num1 = int(input("ingrese un numero entero positivo: "))
num2 = int(input("ingrese un numero entero positivo: "))
num3 = int(input("ingrese un numero entero positivo: "))

if num1 > 0 and num2> 0 and num3> 0:

    print("El cubo del primer numero es ",num1**3)
    print("El cubo del segundo numero es ",num2**3)
    print("El cubo del tercer numero es ", num3**3)
else:
    print("Los numeros tiene que ser enteros")
"""
"""
import random
suma=0.0
for i in range (0,5):
 print("Numeros generados aleatoriamente:")
 num= random.uniform (1,10)
 print ("Numero",i+1,":",num)
 suma+=num
 print("La suma de los números es:", suma)
"""
"""
num1 = int(input("ingrese un numero  "))
num2 = int(input("ingrese un numero  "))
num3 = int(input("ingrese un numero  "))
num4 = int(input("ingrese un numero  "))
num5 = int(input("ingrese un numero  "))

print("lo numeros son ", num1, num2, num3,num4,num5)
print("el numero menor es : ",min (num1,num2,num3,num4,num5) )

"""
"""
#Es el mismo ejercicio anterior usando FOR

numeros = []

for i in range(5):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

menor = numeros[0]  

for num in numeros:
    if num < menor:
        menor = num

print("El número menor es:", menor) 

"""
"""
numeros = []
suma = 0
pares = 0
impares = 0

for i in range(6):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)
    suma += numero

    if  numero % 2 ==0 :
        pares += 1
    else :
        impares += 1

promedio = suma / 6
print ("Los numeros pares son: ", pares)
print ("los numeros impares son: ", impares)
print ("el promedio total es: ", promedio)
"""

import random

numeros = []

for i in range(10):

    numero = random.randint(1,10)
    numeros.append(numero)
print ("Numero generado ",numeros)
print ("El numero maximo de los 10 numeros es ",max(numeros))
print ("El numero minimo de los 10 numeros es ",min(numeros))
print("El número máximo se repite:", numeros.count(max), "veces")
print("El número mínimo se repite:", numeros.count(min), "veces")