peliculas=[]
def borrarPantalla():
    import os
    os.system("cls")
    
def borrarPeliculas():
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

def esperarTecla():
    input("\n\t ... Oprima cualquier tecla para continuar ...")

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


