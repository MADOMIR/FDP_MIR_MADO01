#Importación 
from ClaseVisionQuest import VisionQuest
#from Opcion1 import Opcion1
from Opcion2 import Opcion2

TextoParaBusqueda=""
CantidadDeResultados=0
Enlace=""
NumEnlacesParaAlmacenar=""
VisionQuest1=VisionQuest(TextoParaBusqueda,CantidadDeResultados,Enlace,NumEnlacesParaAlmacenar)

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
       
        TextoParaBusqueda=input("Por favor ingrese el texto para realizar la búsqueda: ")
        EstadoBusqueda="Valor Invalido"
        while EstadoBusqueda=="Valor Invalido":
            CantidadDeResultados=input("Ingrese la cantidad de resultados que desea obtener (max.5): ")
            ListaDeEnlaces,ListaDeEnlacesGenerada,EstadoBusqueda=VisionQuest1.Busqueda(TextoParaBusqueda,CantidadDeResultados)
        if ListaDeEnlacesGenerada:
            for i in ListaDeEnlaces:
             VideoAbierto= VisionQuest1.AbrirVideos(i)
             if VideoAbierto==False:
                 break
        if ListaDeEnlaces and VideoAbierto:
            EstadoDeGuardarEnlace="Valor Invalido"
            while EstadoDeGuardarEnlace=="Valor Invalido":
                NumEnalcesParaAlmacenar=input("Ingrese el número de los enlaces a almacenar, separados por coma (ej. 2,3,n): ")
                EnlacesGuardados,ListaNumEnlacesSinRepetidos,EstadoDeGuardarEnlace=VisionQuest1.GuardarEnlaces(NumEnalcesParaAlmacenar)
                print(EnlacesGuardados)
                print(ListaNumEnlacesSinRepetidos)
                print(EstadoDeGuardarEnlace)  
    #Opcion 2
    if Opcion==2 and ValorOpcionValido==True:
        if EnlacesGuardados==True:
            VideosDescargados=Opcion2(ListaDeEnlaces,ListaNumEnlacesSinRepetidos)
        else:
            print("!!!!Por favor primero ingrese a la opción 1 para realizar una búsqueda")
    #Opción 7
    if Opcion==7 and ValorOpcionValido==True:
        print("Hasta luego que tengas un excelente día")
        Activo=False
