#Importacion de librerías
import webbrowser
from pytube import Search

#Función 
def BusquedaDeVideo(TextoParaBusqueda,CantidadDeResultados):
    ListaDeID=list()
    ListaResBusquedaRaw=Search(TextoParaBusqueda)
    #print(ListaResBusquedaRaw.results)
    #print(len(ListaResBusquedaRaw.results))
    for i in range(0,CantidadDeResultados):
        ListaDeID.append("https://www.youtube.com/watch?v="+str(ListaResBusquedaRaw.results[i])[41:52])
        print("Resultado de video # ",i+1,"- ",ListaDeID[i])
        webbrowser.open(ListaDeID[i], new=1)
    return ListaDeID