from Opcion3 import EscribirArhivo
from Opcion1 import ImpDiaHora
from Opcion2 import AbrirSitioWeb
Activo=True
while Activo==True:
    ValorValido=True
    print("\nIngrese una opción: \nOpción 1: Imprimir día y hora \nOpción 2: Abrir sitio GitHub en explorador \nOpción 3: Escribir texto en archivo \nOpción 4: Salir \n")
    try:
        Opcion=int(input("Ingrese el número de la opción que desea ejecutar: "))
    except:
        print("\n\nValor ingresado inválido por favor ingrese un número entero entre 1 y 4")
        ValorValido=False
    if ValorValido==True:
        if Opcion<1 or Opcion>4:
            print("\n\nValor ingresado inválido por favor ingrese un número entero entre 1 y 4")
            ValorValido=False
        if Opcion==1 and ValorValido==True:
            ImpDiaHora()
        if Opcion==2 and ValorValido==True:
            AbrirSitioWeb()
        if Opcion==3 and ValorValido==True:
            Texto=input("\nIngrese el texto que desea escribir en el archivo: ")
            resultado=EscribirArhivo(Texto) 
            if resultado==True:
                print("\nEl archivo fue escrito con éxito")
            else:
                print("\nEl archivo no pudo ser creado o escrito, por favor pruebe de nuevo")   
        if Opcion==4 and ValorValido==True:
            Activo=False

    
