"""
Ejercicio1

lista = [20, 10, 5, 50, 18, 7, 20, 1, 99, 119]

num = 7
maximo = 0

for item in lista:
    if item > maximo:
        maximo = item

print("El número mayor es:", maximo)

"""

"""
Ejercicio2
lista = [20, 10, 5, 50, 18, 7, 20, 1, 99, 119]

num = 7

    if num in lista:
        print("EL numero 7 esta en la lista")
    else :
        print("El numero 7 no esta en la lista ")

"""

"""
Ejercicio3 

import math

num=float(input("ingrese un numero: "))
raiz=math.sqrt(num)
print(f"la raiz de {num} es {raiz:.2f}")

"""

"""
Ejercicio4

import math

num=float(input("ingrese un numero: "))
raiz=math.sqrt(num)
divisible = False
for i in range (2,int(raiz)):
    if num%i == 0 :
        divisible=True
        break
if divisible==False :
    print("Es primo")
else :
    print("No es primo")

"""

"""
Ejercicio5

import math 

num=float(input("ingrese un numero decimal : "))

arriba=math.ceil(num) 
abajo=math.floor(num)
print(f"Se redondea hacia arriba {arriba} y se redondea hacia abajo {abajo}")
"""

"""
Ejercicio6

import math

num=int(input("ingrese un numero : "))
factorial=math.factorial(num)

print(f"El numero factorial de {num} es {factorial}")

"""
"""
Ejercicio7

import math

num=input("ingrese un angulo en grados : ")
num=float(num.replace("°",""))

seno=math.sin(math.radians(num))
coseno=math.cos(math.radians(num))
tangente=math.tan(math.radians(num))

print (seno,coseno,tangente)
"""
"""
Ejercicio8

palabra=str(input("ingresar una palabra: "))
letra=str(input("ingresar una letra :"))

if letra in palabra :
    print(f"La letra {letra} forma para de la palabra {palabra} :")
    cont=palabra.count(letra)
    print(f"La letra {letra} se repite {cont} veces en la palabra {palabra}")
else :
    print(f"La letra {letra} no forma parte de la palabra {palabra}")

"""
import random
numero= random.randint (0,100)
bandera = False

i=0

while bandera!=True and i<10:
    print("Este es el intento n°:",i+1)
    num=int(input("Ingrese un numero del 1 al 100 : "))
    print("verificando si adivinaste")
    if num==numero:
        print("Felicitaciones Adivinaste ")
        bandera=True
    else :
        if num > numero:
            print("El numero que ingresaste es mas grande que el numero a adivinar")
        else:
            print("El numero que ingresaste es mas chico que el numero a adivinar")
            i+=1
if bandera ==False:
    print("SE terminaron los intnes perdiste ")
