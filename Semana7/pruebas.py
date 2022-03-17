from pytube import YouTube, Stream

lk="https://www.youtube.com/watch?v=xilDDRctnjw"

youtube=YouTube(lk)
video=youtube.streams.first()
print(video.title)
print(video.filesize)
print(video.resolution)

video.download("C:\Temp")


   



        