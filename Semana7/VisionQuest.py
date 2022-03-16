#Importación 
import webbrowser
from Opcion1 import BusquedaDeVideo

#Código
Activo=True
while Activo==True:
    ValorOpcionValido=True
    print("\nIngrese una opción: \nOpción 1: Búsqueda de video \nOpción 2: Descarga de video\
         \nOpción 3: Comprimir y descomprimir videos \nOpción 4: Selección de frames en video\
          \nOpción 5: Identificar contenido en video \nOpción 6: Reporte de contenido\
          \nOpción 7: Salir \n")
    try:
        Opcion=int(input("Ingrese el número de la opción que desea ejecutar: "))
    except:
        print("\n\n!!!!!!!Valor ingresado inválido por favor ingrese un número entero entre 1 y 7")
        ValorOpcionValido=False
    if ValorOpcionValido==True:
        if Opcion<1 or Opcion>7:
            print("\n\n!!!!!!!Valor ingresado inválido por favor ingrese un número entero entre 1 y 7")
            ValorOpcionValido=False
        #Opción 1
        if Opcion==1 and ValorOpcionValido==True:
            TextoParaBusqueda=input("Por favor ingrese el texto para realizar la búsqueda: ")
            ValorCantResValido=False
            while ValorCantResValido==False:
                try:
                    CantidadDeResultados=int(input("Ingrese la cantidad de resultados que desea obtener (max.5): "))
                    if 1<=CantidadDeResultados<=5:
                        ValorCantResValido=True
                        BusquedaDeVideo(TextoParaBusqueda,CantidadDeResultados)
                    else:
                        print("\n\n!!!!!!!Valor ingresado inválido por favor ingrese una cantidad de resultados entero entre 1 y 5")
                except:
                    print("\n\n!!!!!!!Valor ingresado inválido por favor ingrese una cantidad de resultados entero entre 1 y 5")
                    
                
        #Opción 7
        if Opcion==7 and ValorOpcionValido==True:
            Activo=False
