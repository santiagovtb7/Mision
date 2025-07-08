nombres =[]
sueldomensual =[]
sueldoacumulado =[]


for x in range(3): 
    print (f"\nEmpleado:")
    nombre =input ("nombre del empleado: ")
    nombres.append(nombre)
    sueldo1= float (input(f"ingrese el sueldo del mes:"))
    sueldo2= float (input(f"ingrese el sueldo del mes:"))
    sueldo3= float (input(f"ingrese el sueldo del mes:"))
    sueldomensual.append([sueldo1,sueldo2,sueldo3])

    sueldoacumulado.append(sueldo1+sueldo2+sueldo3)

for x in range(3): 
    print(nombres[x])
    print(sueldomensual[x])
    print(sueldoacumulado[x])

#sueldos=[]  


# sueldomensual.append(sueldo)
# sueldoacumulado.append(sum(sueldos))

# print("\n--- sueldos acumulados ---")
# for i in range(3):
#     input(f"{nombre}: ${sueldoacumulado}")