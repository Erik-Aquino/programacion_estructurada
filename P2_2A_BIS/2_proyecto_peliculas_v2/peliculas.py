#Dict u objeto que permita almacenar los siguientes atributos:(nombre, categoria, clasificacion, genero, idioma) de peliculas.

pelicula={
            "nombre":"",
            "categoria":"",
            "clasificaion":"",
            "genero":"",
            "idioma":"",
            }

pelicula={}
def borrarPantalla():
    import os
    os.system("cls")
    
def esperarTecla():
    input("\n\t ... Oprima cualquier tecla para continuar ...")

def crearPeliculas():
    borrarPantalla()
    print("\n\t .:: Agregar Películas ::.\n")
    pelicula.update({"nombre":input("Ingresa el nombre: ").upper().strip()})
    pelicula.update({"categoria":input("Ingresa la categoria: ").upper().strip()})
    pelicula.update({"clasificacion":input("Ingresa la clasificacion: ").upper().strip()})
    pelicula.update({"genero":input("Ingresa el genero: ").upper().strip()})
    pelicula.update({"idioma":input("Ingresa el idioma: ").upper().strip()})
    print("\n\t\t :::¡LA OPERACION SE REALIZO CON ÉXITO! :::")

def mostrarPeliculas():
    borrarPantalla()
    print("\n\t.::Mostrar Peliculas::.\n")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"{i}:{pelicula[i]}")
    else:
        print("\n\t .::no hay peliculas en el sistema::.")

def borrarPeliculas():
    borrarPantalla()
    print("\n\t.::Borrar o quitar pelicula::.\n")
    if len(pelicula)>0:
        resp=input("deseas borrar o quitar la pelicula? (SI/NO)").lower().strip()
        if resp=="si":
            pelicula.clear()
            print("\n\t .::Se realizo con exito la operacion::.")
    else:
        print("\n\t .::no hay peliculas en el sistema::.")

def agregarCaracteristicaPeliculas():
    print("\n\t .:: Agregar Cracteristica ::.\n")
    nuevaCaracteristica=input("Ingresa el nombre de la nueva caracteristisca")
    pelicula.update({"{nuevaCaracteristica}":input(f"Ingresa el/la{nuevaCaracteristica}").upper().strip()})

def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.::Modificar una Caracteristica::.\n")
    for i in pelicula:
        print(f"{i}:  {pelicula[i]}")
        resp=input("Desea modificar el valor de este atributo?: ").lower().strip()
        if resp=="si": 
            atributo_valor=input("Ingrese el nuevo valor: ").upper().strip()
            pelicula[i]=atributo_valor
            print("\n\t\t.::LA OPERACION SE REALIZO CON EXITO!::.")
            esperarTecla()
        borrarPantalla()
        print("\n\t.::Modificar una Caracteristica::.\n")

def borrarCaracteristicaPeliculas():
    borrarPantalla()
    if len(pelicula)<0:
        print("\n\t.::no hay peliculas::.\n")
        for i in range (0,len(pelicula)):
            print(f"{i+1}\t{pelicula[i]}")
    else:
        print("\n\t.::Borrar una Caracteristica::.\n")
        print (pelicula)
        input("Desea borrar alguna caracteristica?").lower().strip()





'''def borrarPeliculas():
    borrarPantalla()
    print("\n\t.::Borrar peliculas::.\n")
    busq=input("Ingrese la pelicula que quiere borrar: ").upper().strip()
    encontro=0
    if not (busq in peliculas):
        print("\n\t.::Esta pelicula no existe en el sistema::.\n")
    else:
        resp="si"
        while busq in peliculas and resp=="si":
            resp=input("Desea actualizar la pelicula? (si/no)").lower()
            if resp=="si":
                posicion=peliculas.index(busq)
                print(f"\nLa pelicula que se borro es {busq} y estaba en la posicion {posicion+1}")
                peliculas.remove(busq)
                encontro+=1
                print("\n\t\t.::LA OPERACION SE REALIZO CON EXITO!::.")
        print(f"\n Se borro {encontro} pelicula(s) con este titulo")
        
def agregarPeliculas():
    borrarPantalla()
    print("\n\t .:: Agregar Películas ::.\n")
    peliculas.append(input("Ingrese el nombre: ").upper().strip())
    print("\n\t\t :::¡LA OPERACION SE REALIZO CON ÉXITO! :::")

def mostrarPeliculas():
    borrarPantalla()
    if len(peliculas)>0:
        print("\n\t.::Mostrar peliculas::.\n")
        for i in range (0,len(peliculas)):
            #peli=peliculas[i]
            print(f"{i+1}\t{peliculas[i]}")
    else:
        print("\n\t.::No hay peliculas por el momento::.\n")

def limpiarPeliculas():
    borrarPantalla()
    print("\n\t .:: Limpiar o borrar TODAS las peliculas ::.\n")
    resp=input("Deseas borrar todas las peliculas del sistema? (Si/No)").lower
    ().strip()
    if resp=="si":
        peliculas.clear()
        print("\n\t\t :::¡LA OPERACION SE REALIZO CON ÉXITO! :::")

def buscarPeliculas():
    borrarPantalla()
    print("\n\t .:: Buscar Peliculas ::.\n")
    pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar: ").upper().strip()
    if not(pelicula_buscar in peliculas):
        print("\n\t .:: Esta pelicula a buscar no existe en el Sistema ::.\n")
    else:
        encontro=0
        for i in range(0,len(peliculas)):
            if pelicula_buscar==peliculas[1]:
                print(f"\n\t La pelicula {pelicula_buscar} se encontro en el casillero: {i+1}")
                encontro+=1
        print(f"\nTenemos {encontro} peliculas(s) con este titulo")
        print("\n\t\t :::¡LA OPERACION SE REALIZO CON ÉXITO! :::")

def modificarPeliculas():
    borrarPantalla()
    print("\n\t .:: Modificar Peliculas ::.\n")
    pelicula_buscar=input("Ingrese el nombre de la pelicula que desea buscar: ").upper().strip()
    encontro=0
    if not(pelicula_buscar in peliculas):
        print("\n\t No se encuentra la apelicula a buscar!")
    else:
        for i in range(0,len(peliculas)):
            if pelicula_buscar==peliculas[1]:
                resp=input("Deseas actualizar la pelicula? (Si/No) ").lower()
                if resp=="si":
                    peliculas[i]=input("\nIntroduce el enuevo nombre de la pelicula: ").upper().strip()
                    encontro+=1
                    print("\n\t\t :::¡LA OPERACION SE REALIZO CON ÉXITO! :::")

    print(f"\nSe modifico {encontro} peliculas(s) con exito")
'''

