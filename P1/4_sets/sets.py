"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
import os
os.system("cls")
os.remove

paises=["México","Brasil","España","Canada","Canada"]
print(paises)

varios={True,"UTD",33,3.14}
print(varios)

#Funciones u Operaciones
paises.append("Mexico")
print(paises)

paises.pop()
print(paises)

paises.remove("Mexico")

#Ejemplo crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados.
resp="si"
emails={""}
while resp=="si":
  emails.add(input("Ingrese su correo: "))
  resp=input("Quiere aregrar otro email? ")

emails_set=set(emails)#Quito los duplicados
emails=list(emails_set)
print(emails)






  



