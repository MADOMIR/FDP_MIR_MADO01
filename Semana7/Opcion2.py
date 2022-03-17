
from pytube import YouTube
import os
# Función para descarga de videos
def Opcion2(ListaDeEnlaces,ListaNumEnlacesSinRepetidos): 
    #Ingreso del número de enlace a descargar y verificación de dato ingresado
    ValorNumEnlaceVideoADescargarValido=False
    while ValorNumEnlaceVideoADescargarValido==False:
        try:
            ValorNumEnlaceVideoADescargarValido=True
            NumEnlaceVideoADescargar=int(input("De la lista de enlaces seleccionado ingrese el número de video a descargar o coloque '0' para descargar todos: "))
            if str(NumEnlaceVideoADescargar) not in ListaNumEnlacesSinRepetidos and NumEnlaceVideoADescargar!=0:
                print("\n!!!!Valor invalido por favor ingrese un valor válido\n")
                ValorNumEnlaceVideoADescargarValido=False
        except:
            print("\n!!!!Valor invalido por favor ingrese un valor válido\n")
            ValorNumEnlaceVideoADescargarValido=False

    #Ingreso de ruta de directorio donde se desea almacenar los videos y verificación de ruta    
    DirectorioValido=False
    while DirectorioValido==False:
        DirectorioValido=True
        DirectorioAlmacenmiento=input("Ingrese el directorio para almacenar los videos: ")
        try:
            if os.path.isdir(DirectorioAlmacenmiento):
                print("Directorio encontrado")
            else:
                print("\n!!!!El directorio no se ha podido encontrar o no existe\n")
                DirectorioValido=False
        except:
            print("\n!!!!El directorio no se ha podido encontrar o no existe\n")
            DirectorioValido=False
    
    #Descarga de todos los videos si la opción 0 fue ingresada
    if NumEnlaceVideoADescargar==0:
        for i in ListaNumEnlacesSinRepetidos:
            try:
                print(".....Descargando")
                YTObj=YouTube(ListaDeEnlaces[int(i)-1])
                video=YTObj.streams.first()
                #print(video.title)
                #print(video.filesize)
                #print(video.resolution)
                
                video.download(DirectorioAlmacenmiento)
                print("El video del enlace ", i," titulado '", video.title, "' fue descargado exitosamente!")
            except:
                print("!!!!!Hubo un problema al descargar el video del enlace ",i, " y no se ha podido descargar el video")
    
    #Descarga del video del número de enlace seleccionado
    else:
        try:
            print(".....Descargando")
            YTObj=YouTube(ListaDeEnlaces[NumEnlaceVideoADescargar-1])
            video=YTObj.streams.first()
            #print(video.title)
            #print(video.filesize)
            #print(video.resolution)
            video.download(DirectorioAlmacenmiento)
            print("El video del enlace ", NumEnlaceVideoADescargar," titulado '", video.title, "' fue descargado exitosamente!")
        except:
            print("!!!!!Hubo un problema y no se ha podido descargar el video")
    return True