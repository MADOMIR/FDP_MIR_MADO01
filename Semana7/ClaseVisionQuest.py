#Importacion de librerías
from ast import Num
import re
import webbrowser
from pytube import Search

class VisionQuest:
    #variables iniciales metodo Busqueda()
    __ListaDeEnlaces=[]
    __ListaDeEnlacesGenerada=False
    __EstadoBusqueda="Inactivo" 
    
    #variables iniciales metodo AbrirVideos()
    __VideoAbierto=False
    __EstadoAbrirVideos="Inactivo" # a usar en un futuro

    #variables iniciales metodo GuardarEnlaces()
    __ListaNumEnlacesSinRepetidos=[]
    __EnlacesGuardados=[]
    __EstadoGuardarEnlaces="Inactivo" 

    #Constructor de inicio
    def __init__(self,pTextoParaBusqueda,pCantidadDeResultados,pEnlace,pNumEnlacesParaAlmacenar):
        self.TextoParaBusqueda=pTextoParaBusqueda
        self.CantidadDeResultados=pCantidadDeResultados
        self.Enlace=pEnlace
        self.NumEnlacesParaAlmacenar=pNumEnlacesParaAlmacenar
    
    @classmethod
    ##### Metodo Busqueda()
    def Busqueda(self, TextoParaBusqueda, CantidadDeResultados):
        #Función busqueda de video
        def BusquedaDeVideo(TextoParaBusqueda,CantidadDeResultados):
            ListaDeEnlaces=[]
            # Busqueda en YouTube y manejo de error en caso no se logre realizar la búsqueda
            try:
                ListaResBusquedaRaw=Search(TextoParaBusqueda)
                for i in range(0,CantidadDeResultados):
                    ListaDeEnlaces.append("https://www.youtube.com/watch?v="+str(ListaResBusquedaRaw.results[i])[41:52])
                    print("Resultado de video # ",i+1,"- ",ListaDeEnlaces[i])
                ListaDeEnlacesGenerada=True
            except:
                print("\n!!!!Error al realizar la búsqueda por favor corrobore su conexión a internet\n")
                ListaDeEnlaces=[]
                ListaDeEnlacesGenerada=False 
            return ListaDeEnlaces,ListaDeEnlacesGenerada
            
        #Asignación de valores ingresados
        self.TextoParaBusqueda=TextoParaBusqueda
        self.CantidadDeResultados=CantidadDeResultados
        try:
            #CantidadDeResultados=int(input("Ingrese la cantidad de resultados que desea obtener (max.5): "))
            CantidadDeResultados=int(CantidadDeResultados)
            if 1<=CantidadDeResultados<=5:
                ListaDeEnlacesYListaDeEnlacesGenerada=BusquedaDeVideo(TextoParaBusqueda,CantidadDeResultados)
                self.__ListaDeEnlaces,self.__ListaDeEnlacesGenerada=ListaDeEnlacesYListaDeEnlacesGenerada
                self.__EstadoBusqueda="Busqueda realizada"
            else:
                print("\n!!!!!!!Valor ingresado inválido por favor ingrese una cantidad de resultados entero entre 1 y 5\n")
                self.__EstadoBusqueda="Valor Invalido"
        except:
            print("\n!!!!!!!Valor ingresado inválido por favor ingrese una cantidad de resultados entero entre 1 y 5\n")
            self.__EstadoBusqueda="Valor Invalido"
        return self.__ListaDeEnlaces,self.__ListaDeEnlacesGenerada, self.__EstadoBusqueda
    
    ##### Metodo AbrirVideos()
    def AbrirVideos(self,Enlace):
        self.Enlace=Enlace
        try:
            webbrowser.open(self.Enlace, new=1)
            self.__VideoAbierto=True
        except:
            print("Error al abrir el enlace "+ Enlace)
            self.__VideoAbierto=False
        return self.__VideoAbierto

    ##### Metodo GuardarEnlaces()
    def GuardarEnlaces(self,NumEnlacesParaAlmacenar):
        if self.__ListaDeEnlacesGenerada:
            self.NumEnlacesParaAlmacenar=NumEnlacesParaAlmacenar
            #Validación numeros de enlaces a almacena del valor ingresado, eliminación de duplicados y resolicitud hasta ingresar dato correcto    
            ListaNumEnlaces=self.NumEnlacesParaAlmacenar.split(",")
            ListaNumEnlacesSinRepetidos=[]
            try:
                for i in range(0,len(ListaNumEnlaces)):
                    iValor=int(ListaNumEnlaces[i])
                    if iValor>len(self.__ListaDeEnlaces) or iValor<=0:
                        print("\n!!!!!El número ", ListaNumEnlaces[i]," no es inválido\n")
                        self.__EstadoGuardarEnlaces="Valor Invalido"
                        break
                    else:
                        self.__EstadoGuardarEnlaces="Valor Valido"        
            except:
                print("\n!!!!!!Valores o formato de datos ingresados no válido\n")
                self.__EstadoGuardarEnlaces="Valor Invalido"
            if self.__EstadoGuardarEnlaces=="Valor Valido":
                for i in ListaNumEnlaces:
                    if i not in self.__ListaNumEnlacesSinRepetidos:
                        self.__ListaNumEnlacesSinRepetidos.append(i)
                for i in ListaNumEnlacesSinRepetidos:
                    print("Enlace de video # ", i," - ", self.__ListaDeEnlaces[int(i)-1] ," - fue almacenado!")
                self.__EnlacesGuardados=True
                self.__EstadoGuardarEnlaces="Enlaces Guardados"
        else:
            self.__ListaNumEnlacesSinRepetidos=[]  
            self.__EnlacesGuardados=False
        return  self.__EnlacesGuardados,self.__ListaNumEnlacesSinRepetidos,self.__EstadoGuardarEnlaces