lado1 =float(input("Ingrese el lado1: "))
lado2 =float(input("Ingrese el lado2: "))
lado3 =float(input("Ingrese el lado3: "))

if lado1==lado2==lado3:
    print("el triangulo es EQUILATERO")
elif lado1 ==lado2 or lado1==lado3 or lado2 == lado3:
    print("El triangulo es isoceles")
else :
    print("El triangulo es escaleno") 