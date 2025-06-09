nombres = []
notas = []
nom=''
cant_aprobados=[]
sum=0
print("Ingrese los datos de 3 alumnos:")
for i in range(3):
    nombre = input("Ingrese un nombre: ")
    nota = float(input("Ingrese la nota de " + nombre + ": "))
    nombres.append(nombre)
    notas.append(nota)
while nom!="salir":
    nom=input("escriba un nombre para mostrar la nota y salir para terminar: ")
    if nom in nombres:
        indice = nombres.index(nom)
        print(f"{nombres[indice]} tiene una nota de {notas[indice]}")
    else:
        print("")
cant_aprobados=0
for nota in notas:
    if nota>=6:
        cant_aprobados+=1
if cant_aprobados==0:
    print("no hay aprobados")
else :
    porcentaje=cant_aprobados/len(notas)*100
print("El porcentaje de aprobados es :",porcentaje)