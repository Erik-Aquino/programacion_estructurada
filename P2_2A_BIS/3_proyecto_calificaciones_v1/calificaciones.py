

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input(f"\n\t🕛  ... Oprima cualquier tecla pra continuar ... 🕛")

def menu_principal():
    print(F"\n\t\t\t📅...:::Sistema de Gestión de calificaiones::...📅\n\n\t1️⃣  Agregar\n\t2️⃣  Mostrar\n\t3️⃣  Cálcular Promedios\n\t4️⃣  buscar\n\t5️⃣  SALIR")
    opcion=input(f"\t\t\t\t👉  Elige una opcion (1-4) ").upper()
    return opcion

def agregarCalif(lista):
    borrarPantalla()
    print("📂  .::Agregar calificaciones::.  📂")
    nombre=input("👤  Ingrese el nombre del alumnos: ").upper().strip()
    calificaciones=[]
    for i in range(1,4):
        continua=True
        while continua:
            try:
                #calificaciones.append(float(input(f"Calificacion #{i}: ")))
                cal=float(input(f"📝 Calificacion #{i}: "))
                if cal>=0 and cal<=10:
                    calificaciones.append(cal)
                    continua=False
                else:
                    print("🚫  Ingresa una calificacion valida del 0 al 10  🚫")
            except ValueError:
                print("Ingresa un valor numerico")
    lista.append([nombre]+calificaciones)
    print("✅  Accion realizada con exito")
    print(lista)

def mostrarCalif(listas):
    borrarPantalla()
    print("📂  .::Mostrar calificaciones::.  📂")
    if len(listas)>=0:
        print(f"{'Nombre':<15}  {'Calif 1':<10}  {'Calif 2':<10}  {'Calif 3':<10}")
        print("-"*45)
        for fila in listas:
            print(f"{fila[0]:<15}  {fila[1]:<10}  {fila[2]:<10}  {fila[3]:<10}")
        print("-"*45)
        print("Son ",len(listas)," Alumnos registrados")
    else:
        print("No hay calificaciones en el sistema")

def calcularCalif(lista):
        borrarPantalla()
        print("📂  .::Promediar a los Alumnos::.  📂")
        if len(lista)>=0:
            print(f"{'Nombre':<15}  {'Promedio':<10} ")
            print("-"*30)
            promedio_grupal=0
            for fila in lista:
                nombre=fila[0]
                #promedio=(fila[1]+fila[2]+fila[3])/3
                promedio=(sum(fila[1:]))/3
                print(f"{nombre:<15}  {promedio:.2f} ")
                promedio_grupal+=promedio
            print("-"*30)
            promedio_grupal=promedio_grupal/len(lista)
            print(f"El promedio del grupo es: {promedio_grupal:.2f}")
        else:
            print("No hay calificaciones en el sistema")

