import os
from pickle import TRUE
def EscribirArhivo(Texto):
    Ruta=os.path.abspath(os.getcwd())+"\Arvhivo.txt"
    try:
        Archivo=open(Ruta,"w")
    except:
         return False
         exit()
    try: 
        Archivo.write(Texto)
        return True
    except:
        return False
    finally:
        Archivo.close

