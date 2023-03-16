numeros=[]
n = int(input("Ingrese la cantidad de numeros que desea operar: "))
mult2=0
mult3=0
mult2y3=0

for i in range(n):
   numero=int(input("ingrese un numero: "))
   numeros.append(numero)

for numero in numeros:
    if numero % 2==0:
        mult2 = mult2+1
    if numero % 3==0:
        mult3 = mult3+1
    if numero % 3==0 and numero % 2==0:
        mult2y3 = mult2y3+1

print(f"Hay {mult2} numeros multiplos de 2, {mult3} numeros multiplos de 3 y {mult2y3} numeros multiplos de ambos")


