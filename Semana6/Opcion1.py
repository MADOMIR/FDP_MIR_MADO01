import datetime
def ImpDiaHora():
    ListaDias={
        0:"domingo",
        1:"lunes",
        2:"martes",
        3:"miercoles",
        4:"jueves",
        5:"viernes",
        6:"sábado",  
    }
    ListaMeses={
        1:"Enero",
        2:"Febrero",
        3:"Marzo",
        4:"Abril",
        5:"Mayo",
        6:"Junio",
        7:"Julio",
        8:"Agosto",
        9:"Septiembre",
        10:"Octubre",
        11:"Noviembre",
        12:"Diciembre",
    }
    FechaHora = datetime.datetime.now()
    print("\nHoy es ",ListaDias.get(int(FechaHora.strftime("%w"))), " ", FechaHora.strftime("%d") ," de",ListaMeses.get(int(FechaHora.strftime("%m"))), " del año", FechaHora.strftime("%Y"))
    print("y son las ",FechaHora.strftime("%I:%M%p"))
