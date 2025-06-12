def contar_pares_impares(lista):
    pares=0
    impares=0

    for numero in lista:
        if  numero % 2 ==0 :
            pares += 1
        else :
            impares += 1

    return pares,impares

if __name__=='__main__':
    
    lista=[]
    valorTabla=int(input("Ingrese la cantidad de  valores de la tabla : "))

    for i in range(valorTabla):
        numeros =int(input("Ingrese un número: "))
        lista.append(numeros)

    pares , impares = contar_pares_impares(lista)

print ("Los numeros pares son: ", pares)
print ("los numeros impares son: ", impares)