Num1=int(input("Ingrese un numero"))
if Num1!=1 or Num1!=2:
    PrimerDato=0
    SegundoDato=1
    print("0 1", end=(" "))
    ListaDeNumeros=(range(3,Num1+1))
    for y in ListaDeNumeros:
        Sucesion=PrimerDato + SegundoDato
        PrimerDato=SegundoDato
        SegundoDato=Sucesion
        print(Sucesion, end=" ")    
else:
    print("Ingrese un número mayor a 2")

