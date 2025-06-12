
def calcular_temp (temp_max, temp_min):
    return (temp_max+temp_min)/2

if __name__=='__main__':
    cont=0
    
    cant_dias=int(input("Ingrese los dias a consultar :"))

    for i in range (cant_dias):
        cant_dias=+1
    
        temp_max=float(input(f"Ingrese la temepratura maxima del dia  {i+1}: "))
        temp_min=float(input(f"Ingrese la temepratura minima del dia  {i+1}: "))

        temp_media=calcular_temp(temp_max, temp_min)

        print(f"la temperatura media del dia {cant_dias} fue {temp_media}°")

   