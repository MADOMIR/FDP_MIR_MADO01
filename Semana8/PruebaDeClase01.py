from ClaseZapato import Zapato
Tenis = Zapato(38,True,350.00)
Tenis.prueba()
print(Tenis._Zapato__color)         # De esta manera podemos igualmente escribir o consultar los atributos ocultos o encapsulados. Pera encontrar como llamarlo correr
                                    # print(dir(Tenis)) en este caso y esto listará los alias de los atributos dentro de los que está el alias del atriburo oculto. 
print(Tenis.AsignarColor("azul"))