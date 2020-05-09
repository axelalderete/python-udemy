#contenido1

print("Datos de la primera persona")
#variables
nombre1=input("ingrese el nombre del producto: ")
precio1=int(input("ingrese un precio: "))
nombre2=input("ingrese el nombre del producto: ")
precio2=int(input("ingrese un precio: "))

#constante
BONIFICAION=20

#PROCESO
precio_total=precio1 + precio2
comparar=precio1 >= precio2
logico=precio1<precio2 and precio1==precio2


cabecera="resultados producto {0} y resultado producto {1}"

print(cabecera. format (nombre1, nombre2))
print("El precio del primer producto es mayor o igual al segundo producto:")
print(comparar)
print("La suma de los productos es:" + str(precio_total))
print("El precio1<precio2 and precio1==precio2: ")
print(logico)

precio_total += BONIFICAION
print("El precio total mas la bonificacion:" +str (precio_total))

