sumatoria=0
sumatoria_por_clave1=0
sumatoria_por_clave2=0
sumatoria_por_clave3=0

print("¿ Qué tipo de clave de Vehiculo Desea determinar el impuesto")
print("1) Clave 1")
print("2) Clave 2")
print("3) Clave 3")
tipo_clave=int(input("Ingrese la clave del vehiculo que desea determinar el impuesto:"))

while tipo_clave>0 and tipo_clave<4:

    if tipo_clave==1:   
        contador_clave1=0
        valor=int(input(" ¿Cuántos vehiculos de clave tipo 1 desea sacar el impuesto? "))
        print()
        while contador_clave1<valor:
            precio_v=float(input(f"Precio\t{contador_clave1+1}"" " "del vehiculo de clave tipo 1:"))
            impuesto=precio_v*0.10
            print(f" El impuesto {contador_clave1+1}  del vehiculo de clave tipo 1 es: {round(impuesto,2)}")
            sumatoria_por_clave1+=impuesto
            contador_clave1+=1

    elif tipo_clave==2:
        contador_clave2=0
        valor=int(input(" ¿Cuántos vehículos de clave tipo 2 desea sacar el impuesto? "))
        print()
        while contador_clave2<valor:
            precio_v=float(input(f"Ingrese el precio{contador_clave2+1}"" " " del vehiculo de clave tipo 2:"))
            impuesto=precio_v*0.07
            print(f" El impuesto{contador_clave2+1} del vehiculo de clave tipo 2 es: {round(impuesto,2)}")
            sumatoria_por_clave2+=impuesto
            contador_clave2+=1
        

    elif tipo_clave==3:
        contador_clave3=0
        valor=int(input(" ¿Cuántos vehículos de clave tipo 3 desea sacar el impuesto? "))
        print
        while contador_clave3<valor:
            precio_v=float(input(f"Ingrese el precio{contador_clave3+1}"" " " del vehiculo clave tipo 3:"))
            impuesto=precio_v*0.05
            print(f" El impuesto {contador_clave3+1} del vehículo de clave tipo 3 es: {round(impuesto,2)}")
            sumatoria_por_clave3+=impuesto
            contador_clave3+=1
        
    else:
        print("Este tipo de clave de vehiculo no existe")
        print("Muchas Gracias")
    
    print("¿Desea sacar el impuesto de otra clave de vehiculo?")
    valor2=input("(Si o No:)")
    print()
    if valor2=='si':
        print("¿ Qué tipo de clave de Vehiculo Desea determinar el impuesto")
        print("1) Clave 1")
        print("2) Clave 2")
        print("3) Clave 3")
        tipo_clave=int(input("Ingrese la clave del vehiculo que desea determinar el impuesto:"))
    else:
        break
sumatoria=sumatoria_por_clave1+sumatoria_por_clave2+sumatoria_por_clave3
print()
print(f"El Impuesto total del vehículo  clave 1 es:{round(sumatoria_por_clave1,2)}")
print(f"El Impuesto total del vehículo  clave 2 es:{round(sumatoria_por_clave2,2)}")
print(f"El Impuesto total del vehículo  clave 3 es:{round(sumatoria_por_clave3,2)}")
print(f"El Impuesto total  de todos los vehiculos que debes pagar es de: {round(sumatoria,2)}")
print("Muchas Gracias") 
