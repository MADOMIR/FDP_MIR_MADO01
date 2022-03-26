
#from pytube import YouTube
#import vlc


#Enlace="https://www.youtube.com/watch?v=1SOuIEi0iFU"
#ObjetoYouTube=YouTube(Enlace)
#video=ObjetoYouTube.streams.get_by_resolution("360p")
#print(len(ObjetoYouTube.streams))
#print("\n",ObjetoYouTube.streams)
#print("\n",video)
#print("\n",video.mime_type)

from re import S
from telnetlib import SE
import cv2 

capture = cv2.VideoCapture('C:\\Temp\\1.mp4')
cont=0
while (capture.isOpened()):
    ret, frame = capture.read()
    if (ret == True):
        cv2.imshow("gato0", frame)
        cont+=1
        Nombre='C:\Temp\imagen'+ str(cont) + '.bmp'
        if cont==1:
            print(Nombre)

        if (cv2.waitKey(30) == ord('c')):
            cv2.imwrite(Nombre, frame)
            print("Captura realizada")
            SeguirCapturando=input("Desea seguir capturando, coloque cualquier texto para contunuar o 's' para salir: ")
            if SeguirCapturando=="s":
                break
        if (cv2.waitKey(30) == ord('s')):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()
