cuentas=[]
n = int(input("Ingrese la cantidad de numeros que desea operar: "))


for i in range(n):
   cuenta={}
   cuenta["numeroCuenta"]=i
   cuenta["saldo"]= int(input("ingrese saldo: "))
   cuentas.append(cuenta)


listanueva=sorted(cuentas, key=lambda x:x["saldo"], reverse=True)
print(listanueva)







