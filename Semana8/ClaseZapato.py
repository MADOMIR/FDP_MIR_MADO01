from unittest.util import _count_diff_all_purpose


class Zapato:

    def __init__(self,pTalla,pEstaEnVenta,pPrecio): #Constructor de inicio. Self direcciona hacia los atributos de la instancia creada. 
                                                    
        self.Talla=pTalla                       #Si requerimos atributos que deban ingresar al crear la instancia se colocan en el parentesis y se declaran
        self.__EstaEnVenta=pEstaEnVenta         # este atributo no puede ser consultado externamente directamente al menos de no de la forma normal pero si es 
                                                # requerido en la generación de la instancia
        self.Precio=pPrecio
        self.__color="No Asigando"              # Este atributo no es requerido en la generación de la instancia pero si forma parte de la instancia de tipo zapato
    @classmethod
    def prueba(cls):
        print("El Zapato Tenis esta en venta: tiene una talla {0} y se vende a un precio de Q.{1}".format(Tenis.Talla,Tenis.Precio))
    def AsignarColor(self, color):
        self.__color=color
        return self.__color
Tenis = Zapato(38,True,350.00)
Tenis.prueba()
print(Tenis._Zapato__color)         # De esta manera podemos igualmente escribir o consultar los atributos ocultos o encapsulados. Pera encontrar como llamarlo correr
                                    # print(dir(Tenis)) en este caso y esto listará los alias de los atributos dentro de los que está el alias del atriburo oculto. 
print(Tenis.AsignarColor("azul"))
