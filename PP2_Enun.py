"""
Se pide desarrollar un programa en Python que permita cargar por teclado
un texto completo en una variable de tipo cadena de caracteres.
El texto finaliza con ‘.’ y se supone que el usuario cargará el
punto para indicar el final del texto, y que cada palabra de ese
texto está separada de las demás por un espacio en blanco.

Informar:
1. Cantidad de palabras con igual cantidad de vocales y consonantes
2. Cantidad de palabras que tienen una cantidad par de dígitos en su composición
3. Cantidad de palabras que contienen al menos una 's' y no contienen ninguna 't'
4. Cantidad de palabras que tienen al menos un dígito en la primera mitad de la palabra

"""


from FuncionesMod import *

item_1 = 0
item_2 = 0
item_3 = 0
item_4 = 0

cantidad_vocales = 0
cantidad_consonantes = 0
cantidad_digito = 0
posicion_digito = None
cantidad_letdig = 0
flag_s = False
contador_t = 0


texto = input("Ingrese el texto a analizar:")

for car in texto :
    if car != " " and car != "." :

        cantidad_digito += 1
        if es_letra(car):
            if es_vocal(car):
                cantidad_vocales += 1
            else:
                cantidad_consonantes += 1
        if es_digito(car):
            cantidad_digito += 1
            if posicion_digito is None :
                posicion_digito = cantidad_letdig
        if car == "s" or car == "S":
            flag_s = True
        if car.lower == "t":
            contador_t += 1

    else: # termina la palabra

        if cantidad_vocales > 0 and cantidad_vocales == cantidad_consonantes :
            item_1 += 1

        if cantidad_letdig > 0 and cantidad_letdig%2 == 0:
            item_2 += 1

        if flag_s > True and contador_t == 0:
            item_3 += 1

        if posicion_digito is not None and posicion_digito <= (cantidad_letdig//2):
            item_4 += 1


        #reset antes q comience la proxima palabra

        cantidad_vocales = 0
        cantidad_consonantes = 0
        cantidad_digito = 0
        posicion_digito = None
        cantidad_letdig = 0
        flag_s = False
        contador_t = 0




print("Cantidad de palabras con igual cantidad de vocales y consonantes", item_1)
print("cantidada de palabras con par digitos", item_2 )
print("Cantidad de palabras que contienen al menos una 's' y no contienen ninguna 't'", item_3)
print("Cantidad de palabras que tienen al menos un dígito en la primera mitad de la palabra", item_4)
