
from pytube import YouTube
import os

def Opcion2(ListaDeEnlaces,ListaNumEnlacesSinRepetidos):  
    ValorNumEnlaceVideoADescargarValido=False
    while ValorNumEnlaceVideoADescargarValido==False:
        try:
            ValorNumEnlaceVideoADescargarValido=True
            NumEnlaceVideoADescargar=int(input("De la lista de enlaces seleccionado ingrese el número de video a descargar o coloque '0' para descargar todos: "))
            if str(NumEnlaceVideoADescargar) not in ListaNumEnlacesSinRepetidos and NumEnlaceVideoADescargar!=0:
                print("!!!!Valor invalido por favor ingrese un valor válido")
                ValorNumEnlaceVideoADescargarValido=False
        except:
            print("!!!!Valor invalido por favor ingrese un valor válido")
            ValorNumEnlaceVideoADescargarValido=False

    DirectorioValido=False
    while DirectorioValido==False:
        DirectorioValido=True
        DirectorioAlmacenmiento=input("Ingrese el directorio para almacenar los videos: ")
        try:
            if os.path.isdir(DirectorioAlmacenmiento):
                print("Directorio encontrado")
            else:
                print("El directorio no se ha podido encontrar o no existe")
                DirectorioValido=False
        except:
            print("El directorio no se ha podido encontrar o no existe")
            DirectorioValido=False

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