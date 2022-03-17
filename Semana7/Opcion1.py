#Importacion de librerías
import webbrowser
from pytube import Search



#Función busqueda de video
def BusquedaDeVideo(TextoParaBusqueda,CantidadDeResultados):
    ListaDeEnlaces=[]
    # Busqueda en YouTube y manejo de error en caso no se logre realizar la búsqueda
    try:
        ListaResBusquedaRaw=Search(TextoParaBusqueda)
        #print(ListaResBusquedaRaw.results)
        #print(len(ListaResBusquedaRaw.results))
        for i in range(0,CantidadDeResultados):
            ListaDeEnlaces.append("https://www.youtube.com/watch?v="+str(ListaResBusquedaRaw.results[i])[41:52])
            print("Resultado de video # ",i+1,"- ",ListaDeEnlaces[i])
            webbrowser.open(ListaDeEnlaces[i], new=1)
        ListaDeEnlacesGenerada=True
    except:
        print("\n!!!!Error al realizar la búsqueda por favor corrobore su conexión a internet\n")
        ListaDeEnlaces=[]
        ListaDeEnlacesGenerada=False 
       
    return ListaDeEnlaces,ListaDeEnlacesGenerada

# Funcion busqueda, despliegue y almacenamiento de enlaces de videos
def Opcion1():  
    #Ingreso de texto para búsqueda
    TextoParaBusqueda=input("Por favor ingrese el texto para realizar la búsqueda: ")

    #Ingreso de cantidad de resultados, validación del valor ingresado y resolicitud hasta ingresar un valor correcto
    ValorCantResValido=False
    while ValorCantResValido==False:
        try:
            CantidadDeResultados=int(input("Ingrese la cantidad de resultados que desea obtener (max.5): "))
            if 1<=CantidadDeResultados<=5:
                ValorCantResValido=True
                ListaDeEnlacesYListaDeEnlacesGenerada=BusquedaDeVideo(TextoParaBusqueda,CantidadDeResultados)
                ListaDeEnlaces,ListaDeEnlacesGenerada=ListaDeEnlacesYListaDeEnlacesGenerada
            else:
                print("\n!!!!!!!Valor ingresado inválido por favor ingrese una cantidad de resultados entero entre 1 y 5\n")
        except:
            print("\n!!!!!!!Valor ingresado inválido por favor ingrese una cantidad de resultados entero entre 1 y 5\n")
    if ListaDeEnlacesGenerada:
        #Almacenamiento de enlaces de videos
        #Ingreso de numeros de enlaces a almacenar, validación del valor ingresado, eliminación de duplicados y resolicitud hasta ingresar dato correcto
        ValorNumEnlacesValido=False	
        while ValorNumEnlacesValido==False:
            ValorNumEnlacesValido=True
            NumsEnalcesParaAlmacenar=input("Ingrese el número de los enlaces a almacenar, separados por coma (ej. 2,3,n): ")
            ListaNumEnlaces=NumsEnalcesParaAlmacenar.split(",")
            ListaNumEnlacesSinRepetidos=[]
            try:
                for i in range(0,len(ListaNumEnlaces)):
                    iValor=int(ListaNumEnlaces[i])
                    if iValor>len(ListaDeEnlaces) or iValor<=0:
                        print("\n!!!!!El número ", ListaNumEnlaces[i]," no es inválido\n")
                        ValorNumEnlacesValido=False
                for i in ListaNumEnlaces:
                    if i not in ListaNumEnlacesSinRepetidos:
                        ListaNumEnlacesSinRepetidos.append(i)
            except:
                print("\n!!!!!!Valores o formato de datos ingresados no válido\n")
                ValorNumEnlacesValido=False
        for i in ListaNumEnlacesSinRepetidos:
            print("Enlace de video # ", i," - ", ListaDeEnlaces[int(i)-1] ," - fue almacenado!")
        EnlacesGuardados=True
    else:
        ListaDeEnlaces=[]
        ListaNumEnlacesSinRepetidos=[]  
        EnlacesGuardados=False 
    return ListaDeEnlaces,ListaNumEnlacesSinRepetidos,EnlacesGuardados