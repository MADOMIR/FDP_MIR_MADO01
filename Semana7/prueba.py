
#from pytube import YouTube
#import vlc


#Enlace="https://www.youtube.com/watch?v=1SOuIEi0iFU"
#ObjetoYouTube=YouTube(Enlace)
#video=ObjetoYouTube.streams.get_by_resolution("360p")
#print(len(ObjetoYouTube.streams))
#print("\n",ObjetoYouTube.streams)
#print("\n",video)
#print("\n",video.mime_type)

import cv2 

capture = cv2.VideoCapture('C:\\Temp\\1.mp4')

while (capture.isOpened()):
    ret, frame = capture.read()
    if (ret == True):
        cv2.imshow("gato0", frame)
        if (cv2.waitKey(30) == ord('s')):
            break
    else:
        break

capture.release()
a=input("cualuier tecla")
cv2.destroyAllWindows()
