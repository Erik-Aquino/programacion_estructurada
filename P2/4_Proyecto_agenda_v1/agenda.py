
'''
contactos={
        "Ruben":["6181111111","ruben@gmail.com"]
        ¨Daniel

}
'''


def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input(f"\n\t\t\U0001F552 Oprima cualquier tecla pra continuar ...")

def menu_principal():
    print(F"\n\t\t\t\U0001F4DE Sistema de gestion de agenda de contactos  \U0001F4DE\n\n\t1\uFE0F\u20E3\tAgregar contacto \n\t2\uFE0F\u20E3\tMostrar todos los contactos\n\t3\uFE0F\u20E3\tBuscar contacto por nombre\n\t4\uFE0F\u20E3\tModificar contacto: \n5.-  Borrar contacto: \n6.- Salir")
    opcion=input(f"\t\t\U0001F4DD Elige una opcion (1-6): ").upper()
    return opcion

def agregarContac(agenda):
    borrarPantalla()
    print("\t\t Agregar contactos ")
    nombre=input("Ingrese su nombre: ").upper().strip()
    if nombre in agenda:
        print("Este contacto ya existe")
    else:
        telefono=input("Ingrese su numero de telefono: ").upper()
        email=input("Ingrese su correo electronico: ").lower().strip()
        agenda[nombre]=[telefono,email]
        print("Operacion realizada con exito")
    print("")


def mostrarContac(agenda):
    borrarPantalla()
    print("\t\t Mostrar contactos ")
    if not agenda:
        print("La agenda esta vacia")
    else:
        print(f"{'NOMBRE':<15} {'TELEFONO':<15} {'EMAIL':<10}")
        print(f"-"*45)
        for nombre,fila in agenda.items():
            print(f"{nombre:<15} {fila[0]:<15} {fila[1]:<10}")
            print(f"-"*45)
    print("")

def buscarContac(agenda):
    borrarPantalla()
    print("\t\t Mostrar contactos ")
    if not agenda:
        print("La agenda esta vacia")
    else:
        nombre=input("Introduzca el nombre a buscar: ").upper().strip()
        if nombre in agenda:
            print(f"{'NOMBRE':<15} {'TELEFONO':<15} {'EMAIL':<10}")
            print(f"-"*45)
            for nombre,fila in agenda.items():
                print(f"{nombre:<15} {fila[0]:<15} {fila[1]:<10}")
                print(f"-"*45)
        else:
            print("No se encontro este nombre ")

def modificarContac(agenda):
    borrarPantalla()
    print("\t\t Modificar contactos ")
    if not agenda:
        print("La agenda esta vacia")
    else:
        nombre=input("Introduce el nombre al que le deseas modificar sus atributos: ").upper().strip()
        for i in agenda:
            if nombre in agenda:
                print("Valores actuales")
                print(f"Nombre: {nombre}\nTelefono: {agenda[nombre][0]}\nE-mail: {agenda[nombre][1]}")
                resp=input("Deseas cambiar los valores? (SI/NO)").lower().strip()
                if resp=="si":
                    telefono=input("Telefono: ").upper()
                    email=input("E-mail: ").lower().strip()
                    agenda[nombre]=[telefono,email]
                    print("Accion realizada con éxito")
            else:
                print("Este contacto no exite")
                
                

def borrarContac(agenda):
    borrarPantalla()
    print("\t\t Borrar contacto ")
    if not agenda:
        print("La agenda esta vacia")
    else:
        nombre=input("Introduce el nombre del contacto a eliminar: ").upper().strip()
        if nombre in agenda:
            agenda[nombre]=[]
            agenda.pop(nombre)