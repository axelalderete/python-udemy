def es_vocal(letra):
    return letra.lower() in "aeiouáéíóúü"


def es_letra(caracter):
    return caracter.lower() in "abcdefghijklmnñopqrstuvwxyz"


def es_consonante(letra):
    return es_letra(letra) and not es_vocal(letra)


def es_digito(caracter):
    return caracter in "0123456789"


def test():
    print(es_vocal("A"))
    print(es_vocal("B"))
    print("---")
    print(es_letra("W"))
    print(es_letra("-"))
    print("---")
    print(es_consonante("S"))
    print(es_consonante("A"))
    print(es_consonante("-"))
    print("---")
    print(es_digito("5"))
    print(es_digito("w"))

if __name__ == "__main__":
    test()

