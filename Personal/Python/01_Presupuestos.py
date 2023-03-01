#Se insertan los datos a traves de un input 
presupuesto_enero = input("¿cual es tu /n presupuesto en enero?")
presupuesto_febrero = input("¿cual es tu presupuesto en febrero?")
presupuesto_marzo = input("¿cual es tu presupuesto en marzo?")
#Se aclara que los tipos de datos son enteros
presupuesto_enero = int(presupuesto_enero)
presupuesto_febrero = int(presupuesto_febrero)
presupuesto_marzo = int(presupuesto_marzo)
#Se muestra en pantalla como cada dato fue ingresado de manera correcta
print("tu presupuesto de enero es:", presupuesto_enero)
print("tu presupuesto de febrero es:",presupuesto_febrero)
print("tu presupuesto de marzo es:",presupuesto_marzo)
#Se realiza la operacion de promedio de cada presupuesto 
presupuesto_promedio = (presupuesto_enero + presupuesto_febrero + presupuesto_marzo)/3
print (f"el presupuesto promedio para los 3 primero meses es de:, {presupuesto_promedio}")
#revusion del tipo de variable resultado
print(type(presupuesto_promedio))