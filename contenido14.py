def cargar():
    diccionario={}
    continua="s"
    while continua=="s":
        caste=input("ingrese palabra en castellano:")
        ing=input("ingrese palabra en ingles:")
        diccionario[caste]=ing
        continua=input("quiere cargar otra plabra:[s/n]")
    return diccionario

def imprimir(diccionario):
    print("listado completo del diccionario")
    for ingles in diccionario:
        print(ingles,diccionario[ingles])

def consulta_palabra(diccionario):
    pal=input("ingrese la palabra en castellano a consultar:")
    if pal in diccionario:
        print("en ingles significa:",diccionario[pal])

diccionario=cargar()
imprimir(diccionario)
consulta_palabra(diccionario)




