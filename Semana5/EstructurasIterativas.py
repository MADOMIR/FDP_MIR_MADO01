#Conteo de dígitos
Num1=int(input("Escriba un numero: "))
ConteoDigitos=0
Numero=Num1
while(Numero!=0):
    ConteoDigitos+=1
    Numero=Numero//10
print("El número ", Num1,"tiene ",ConteoDigitos,"Dígitos")
#Conteo de número pares e impares
Num1=int(input("Escriba un numero:"))
Listado=list(range(1,Num1+1))
ContadorPares=0
ContadorImpares=0
for i in Listado:
    if(i%2==0):
        ContadorPares+=1
    else:
        ContadorImpares+=1
print("Impares ",ContadorImpares)
print("Pares ",ContadorPares)

#Ciclos anidados
Num1=int(input("Escriba un numero:"))
for i in range(1,Num1+1):
    for y in range(1,i+1):
        print(y, end=" ")
    print("")
