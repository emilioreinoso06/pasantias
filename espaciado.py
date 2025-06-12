def ConvertirEspaciado(texto):
    resultado= ""
    for letra in texto:
        resultado += letra +  " "
    return resultado
if __name__=='__main__':
    texto=str(input("Ingrese un texto : "))
    textoEspaciado=ConvertirEspaciado(texto)
    print(f"El texto con los espacios es {textoEspaciado}")


