#contenido2


sueldo=int(input("Ingrese el sueldo:"))

if sueldo>3000:
    print("El usuario debe pagar un porcentaje en impuestos")
if sueldo<=3000:
    print("El usuario esta exento de declarar su renta ")
if sueldo>6000 and sueldo<10000:
    print("El usuario tiene que pagar una bonificacion de 1000 euros")
if sueldo == 20000 or sueldo == 30000:
    print("El usuario debe pagar el 10% del sueldo")
