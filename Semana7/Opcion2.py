
from ast import Num
from pytube import YouTube
import os
import vlc

# Función para descarga de videos
def Opcion2(ListaDeEnlaces,ListaNumEnlacesSinRepetidos): 
    #Ingreso del número de enlace a descargar y verificación de dato ingresado
    ValorNumEnlaceVideoADescargarValido=False
    while ValorNumEnlaceVideoADescargarValido==False:
        try:
            ValorNumEnlaceVideoADescargarValido=True
            NumEnlaceVideoADescargar=int(input("De la lista de enlaces guardados ingrese el número de video a descargar o coloque '0' para descargar todos: "))
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
    ListaDeNombresDeVideos=[]
    ListaDeEnlacesDescargados=[]
    if NumEnlaceVideoADescargar==0:
        for i in ListaNumEnlacesSinRepetidos:
            try:
                print(".....Descargando")
                #print(ListaDeEnlaces[int(i)-1])
                YTObj=YouTube(ListaDeEnlaces[int(i)-1])
                video=YTObj.streams.get_by_resolution("360p")
                #print(video.title)
                #print(video.filesize)
                #print(video.resolution)
                #print(video.codecs)
                #print(video.fps)
                #print(video.itag)
                #print(video.abr)
                #print(video.video_codec)
                video.download(DirectorioAlmacenmiento)
                print("El video del enlace ", i," titulado '", video.title, "' fue descargado exitosamente!")
                ListaDeNombresDeVideos.append(video.title)
                ListaDeEnlacesDescargados.append(i)
                DescargaExitosa=True
            except:
                print("!!!!!Hubo un problema al descargar el video del enlace ",i, " y no se ha podido descargar el video")
                DescargaExitosa=False
                break
    #Descarga del video del número de enlace seleccionado
    else:
        try:
            print(".....Descargando")
            YTObj=YouTube(ListaDeEnlaces[NumEnlaceVideoADescargar-1])
            video=YTObj.streams.get_by_resolution("360p")
            #print(video.title)
            #print(video.filesize)
            #print(video.resolution)
            
            video.download(DirectorioAlmacenmiento)
            print("El video del enlace ", NumEnlaceVideoADescargar," titulado '", video.title, "' fue descargado exitosamente!")
            ListaDeNombresDeVideos.append(video.title)
            ListaDeEnlacesDescargados.append(NumEnlaceVideoADescargar)
            DescargaExitosa=True
        except:
            print("!!!!!Hubo un problema y no se ha podido descargar el video")
            DescargaExitosa=False

    #Consulta si desea reproducir un video
    ReproducirVideoAlmacenado=input("¿Desea reproducir alguno de los videos descargados? (y/n): ")
    if ReproducirVideoAlmacenado=="y":
        #Ingreso del número de video a visualizar y verificación de dato ingresado
        ValorNumVideoVisualizarValido=False
        if DescargaExitosa ==True:
            while ValorNumVideoVisualizarValido==False:
                try:
                    ValorNumVideoVisualizarValido=True
                    NumVideoAVisualizar=int(input("De la lista de videos descargados ingrese el número de video que desea repropducir: "))
                    if NumVideoAVisualizar not in ListaDeEnlacesDescargados:
                        print("\n!!!!Valor invalido por favor ingrese un valor válido\n")
                        ValorNumVideoVisualizarValido=False
                except:
                    print("\n!!!!Valor invalido por favor ingrese un valor válido\n")
                    ValorNumVideoVisualizarValido=False
         #Reproduce todos los videos si la opción 0 fue ingresada
        if NumVideoAVisualizar==0:
            print(ListaDeNombresDeVideos)
            print(ListaDeEnlacesDescargados)
              
        #Reproduce el video del número de enlace seleccionado
        else:
            print(ListaDeNombresDeVideos)
            print(ListaDeEnlacesDescargados)
            #RutaVideoAAbrir= DirectorioAlmacenmiento+"\\"+ListaDeNombresDeVideos[NumVideoAVisualizar]+".mp4"
            #print(RutaVideoAAbrir) 
            #media=vlc.MediaPlayer(DirectorioAlmacenmiento+"\\"+ListaDeEnlaces[NumVideoAVisualizar]+".3gpp")  
            #media.play()
    elif ReproducirVideoAlmacenado!="n":
        print("\n!!!!!Valor ingresado inválido por favor ingrese y ó n")
   
    return DescargaExitosa

    ###### Queda pendiente abri y reproducir los videos pero antes generar los metodos de la opción dos en la clase VisionQuest