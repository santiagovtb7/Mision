# nombredepadres =[]
# hijos =[]

# for x in range(2): 
#     print (f"\padre:")
#     nombre =input ("nombre del padre: ")
#     nombredepadres.append(nombre)
#     hijos1= float (input(f"ingrese el nombre del hijo:"))
#     hijos2= float (input(f"ingrese el nombre del hijo:"))
#     hijos3= float (input(f"ingrese el nombre del hijo:"))
#     hijos.append(hijos1,hijos2,hijos3)

     
#     print (nombredepadres[x])
#     print (hijos[x])

#     #nombresdepadres[]

 
nombre_padres = []
nombre_hijos =[]
for i in range(1):
    madre = input("ingrese el nombre de la madre:\n")
    nombre_padres.append(madre)
    padre = input("ingrese le nombre del padre:\n ")
    nombre_padres.append(padre)
    n = int(input("¿Cuantos hijos tiene?"))
    for j in range(n):
        nombre_hijo = input("Ingrese el nombre del hijo")
        nombre_hijos.append(nombre_hijo)
 
print(nombre_padres)
print(nombre_hijos)