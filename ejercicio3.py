opcion = 1
ciclistas = []
iterador = 0
seEncontro=False

print("*****Ciclistas Giro Italia*****")
print("1: Registrar tiempo")
print("2: Mostrar tabla posiciones")
print("3: Editar tiempos")
print("4: Eliminar registro")
print("0: Salir")

while opcion!=0:
    opcion=int(input("Favor ingrese la opcion deseada: ")) 
    iterador=iterador+1
    if opcion == 1 :
        #Agregando una ciclista al arreglo de ciclistas
        ciclista={}
        ciclista["id"]=iterador
        ciclista["nombre"]=input("Digita el nombre de la ciclista: ")
        ciclista["edad"]=int(input("Digita la edad del ciclista: "))
        ciclista["pais"]=input("Digita el pais del ciclista: ")
        ciclista["equipo"]=input("Digita el equipo del ciclista: ")
        ciclista["tiempo"]=int(input("Digita el tiempo del ciclista: "))
        ciclistas.append(ciclista)
        
    elif opcion == 2 :
        for ciclista in ciclistas:
            print(ciclista)        
        
    elif opcion == 3 :
        buscarciclista=int(input("Digita el codigo de la ciclista a buscar: "))
        for ciclistaSeleccionada in ciclistas:
            if ciclistaSeleccionada["id"] == buscarciclista :
                ciclistaSeleccionada["tiempo"]=float(input("Digite el nuevo tiempo: "))
                seEncontro=True
            else: seEncontro=False
        if seEncontro==False:
            print("La ciclista no se ha encontrado")
            

    elif opcion == 4 :
        buscarciclista=int(input("Digita el codigo de la ciclista a eliminar: "))
        for ciclistaSeleccionada in ciclistas:
            if ciclistaSeleccionada["id"] == buscarciclista :
                ciclistas.remove(ciclistaSeleccionada)
            else: seEncontro=False
        if seEncontro==False:
            print("La ciclista no se ha encontrado")

    elif opcion == 0 :
        print("fue un placer!")
    else:
        print("Digita una opcion valida")
         
    

