import datetime
def ImpDiaHora():
    FechaHora = datetime.datetime.now()
    print("\nHoy es ",FechaHora.strftime("%A"), " ", FechaHora.strftime("%d") ," de",FechaHora.strftime("%B"), " del año", FechaHora.strftime("%Y"))
    print("y son las ",FechaHora.strftime("%I:%M%p"))
