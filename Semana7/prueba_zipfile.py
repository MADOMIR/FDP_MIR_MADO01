import zipfile
import os
print(os.getcwd())
os.chdir("C:\\Temp")
#Cambiar el directorio de trabajo
print(os.getcwd())
#Crea una instancia de ZipFile para escritura el atributo 1 es el archivo zip que se creará en conjunto con su ruta
jungle_zip = zipfile.ZipFile('C:\\Temp\\Comprimido\\1.zip', 'w')
#Comprime el archivo del atributo 1 en este caso está en el directorio de trabajo seleccionado
jungle_zip.write('1.mp4', compress_type=zipfile.ZIP_DEFLATED)
a=input("cualquier cosa para seguir:")
#Crea una instancia de Zipfile para lectura el atributo 1 es el archivo zip que se desea descomprimir
jungle_zip = zipfile.ZipFile('C:\\Temp\\Comprimido\\1.zip', 'r')
#Extrae el arhivo en la ruta ingresada en el atributo
jungle_zip.extractall('C:\\Temp\\Extraido\\') 
#Cierra la instancia creada
jungle_zip.close()