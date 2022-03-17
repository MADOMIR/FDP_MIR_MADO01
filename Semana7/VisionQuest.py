#Importación 
import webbrowser
from Opcion1 import Opcion1
from Opcion2 import Opcion2

#Código
Activo=True
EnlacesGuardados=False
while Activo==True:
    #Impresión ciclica de menú de opciones 
    ValorOpcionValido=True
    print("\nIngrese una opción: \nOpción 1: Búsqueda de video \nOpción 2: Descarga de video\
         \nOpción 3: Comprimir y descomprimir videos \nOpción 4: Selección de frames en video\
          \nOpción 5: Identificar contenido en video \nOpción 6: Reporte de contenido\
          \nOpción 7: Salir \n")
    #Solicitud de ingreso de opción y validación de valor de opción ingresada
    try:
        Opcion=int(input("Ingrese el número de la opción que desea ejecutar: "))
    except:
        print("\n\n!!!!!!!Valor ingresado inválido por favor ingrese un número entero entre 1 y 7")
        ValorOpcionValido=False
    if (ValorOpcionValido==True) and (Opcion<1 or Opcion>7):
         print("\n\n!!!!!!!Valor ingresado inválido por favor ingrese un número entero entre 1 y 7")
         ValorOpcionValido=False

    #Opción 1
    if Opcion==1 and ValorOpcionValido==True:
        ListaYNumerosDeEnlacesSeleccionados=Opcion1()
        ListaDeEnlaces,ListaNumEnlacesSinRepetidos,EnlacesGuardados=ListaYNumerosDeEnlacesSeleccionados
    #Opcion 2
    if Opcion==2 and ValorOpcionValido==True:
        if EnlacesGuardados==True:
            VideosDescargados=Opcion2(ListaDeEnlaces,ListaNumEnlacesSinRepetidos)
        else:
            print("!!!!Por favor primero ingrese a la opción 1 para realizar una búsqueda")
    #Opción 7
    if Opcion==7 and ValorOpcionValido==True:
        Activo=False
