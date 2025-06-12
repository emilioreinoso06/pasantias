def calcularMaxMin(lista):
    num_max=max(lista)
    num_min=min(lista)
    return num_max,num_min
if __name__=='__main__':

    lista=[]
    valorTabla=int(input("Ingrese la cantidad de  valores de la tabla : "))

    for i in range(valorTabla):
        numero=input("Ingrese los numeros a la tabla : ")
        lista.append(numero)
    print(f"Los numeros de la tabla son {lista}")
    num_max=max(lista)
    num_min=min(lista)
print(f"El numero mayor es :{num_max} y el numero minimo es : {num_min}")
