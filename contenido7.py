lista = []
for k in range(10):
    lista.append(input("agregue valor a la lista: "))

print("los elementos de la lista son:"+str(lista))
valor=int(input("introduce el valor a modificar pon el indice:"))
nuevo=input("ingresa el nuevo valor:")
lista[valor]= nuevo
print("los elementos de la lista son:" +str(lista))
valor=int(input("inserta el indice donde se inserta el nuevo valor:"))
nuevo=input("inserta el nuevo valor:")
lista.insert(valor,nuevo)
print("los elementos de la lista son:" +str(lista))
nuevo=input("introduce el valor a aliminar:")
lista.remove(nuevo)
print("los elementos de la lista son:" +str(lista))
nuevo=input("inserta el valor que quieres buscar")
resultado=(nuevo in lista)
if (resultado):
    print("existe este elemento y su indice es:" +str(lista.index(nuevo)))
else:
    print("no existe este elemento")



