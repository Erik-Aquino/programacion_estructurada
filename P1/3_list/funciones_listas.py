'''
List (Array)
Son colecciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace un indice numerico

Nota: Sus valores si sin modificables

La lista es una coleccion ordenanda y modificable. Permite miembros duplicados.
'''


import os
os.system('cls')

#Funciones mas comunes en las listas
paises=["Mexico", "España","Brasil","Canada"]

numeros=[23,45,8,24]

varios=["hola",3.1416,33,True]

#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)

#Recorrer la lista
#1er forma
for i in paises:
    print (i)

#2do forma

for i in range(0,len(paises)):
    print(paises[i])

#Ordenar elementos de una lista
paises.sort()
print(paises)
numeros.sort
print(numeros)

#Dar la vuelta a una vista
paises.reverse
print(numeros)

varios.reverse()
print(varios)

#Agregar, insertar, añadir un elemento a una lista
#1er forma
paises.append("Honduras")
print(paises)

#2da forma
paises.insert(1,"Honduras")
print(paises)

paises.sort()
print(paises)

#Elminar, borrar, suprimir, un elemnto de una lista
#1er forma
paises.pop(4)
print(paises)

#2da forma
paises.remove("Honduras")
print(paises)

#Buscar un elemento dentro de la lista
print(paises)

print("Brasil" in paises)

#Contar el numero de veces que aparece un elemento en una lista

print(numeros)

cuantos=numeros.count(23)
print(cuantos)

numeros.append(23)
cuantos=numeros.count(23)
print(cuantos)

#Conocer la posicion o indice en el que se encuenra un elemento de la lista
paises.reverse
print(paises)

posicion=paises.index("Canada")
print(f"El valor de Canada lo encontro en la posicion: {posicion}")

#unir el contenido de una lista dentro de otra lista

print(numeros)
numeros2=[100,200]

print(numeros2)

#Crear a partir de las lsitas de numeros de 1 y 2 un resultante y mostrar el contenido ordenado descendentemente
#os.system("cls")
numeros.extend(numeros2)
print(numeros)

numeros.sort()
print(numeros)

numeros.reverse()
print(numeros)