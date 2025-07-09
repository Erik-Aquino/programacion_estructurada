import calificaciones

def main():
    datos=[]

    opcion=True

    while opcion:
        calificaciones.borrarPantalla()
        opcion=calificaciones.menu_principal()

        match opcion:
            case "1":
                calificaciones.agregarCalif(datos)
                calificaciones.espereTecla()
            case "2":
                calificaciones.mostrarCalif(datos)
                calificaciones.espereTecla()
            case "3":
                calificaciones.calcularCalif(datos)
                calificaciones.espereTecla()
            case "4":
                opcion=False
                print(F"\n\t🚪 Terminaste la ejecucion del Sistema... Gracias 🚪")
            case _ : 
                opcion=True
                calificaciones.espereTecla()
                print("\n\t❌ Opcion invalida vuelva a intentarlo ❌")
if __name__=="__main__":
    main()