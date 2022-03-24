from pytube import Search
from pytube import YouTube
import os
EnlaceParaDescarga=input("Por favor pegue el enlace del video que desea descargar: ")
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
try:
    print(".....Descargando")
    YTObj=YouTube(EnlaceParaDescarga)
    video=YTObj.streams.get_highest_resolution()
    #print(video.title)
    print(video.filesize)
    print(video.resolution)
    
    video.download(DirectorioAlmacenmiento)
    print("El video del enlace titulado '", video.title, "' fue descargado exitosamente!")
except:
    print("!!!!!Hubo un problema al descargar el video del enlace y no se ha podido descargar el video")