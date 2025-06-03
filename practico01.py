radio = float (input("Ingrese el radio: "))
altura = float (input("Ingrese la altura: "))

pi = 3.14

volumen = pi*(radio**2)*altura


if (volumen>300):
    print(volumen)
else:
    print("Valor incorrecto ")
