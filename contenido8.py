#funciones
def presentacion():
    print("presentacion de funciones")
    print("********************************")
def introducir_datos():
    global valor1
    global valor2
    valor1=int(input("ingrese el primer valor: "))
    valor2=int(input("ingrese el segundo valor: "))
def suma():
    suma = valor1+valor2
    print("la suma es:" ,suma)
def resta():
    resta= valor1-valor2
    print("la resta es",resta)
def multiplicacion():
    multiplicacion=valor1*valor2
    print("lamultiplicaion es:",multiplicacion)
def finalizacion():
    print("gracias por utilizar este programa")


presentacion()
introducir_datos()
suma()
resta()
multiplicacion()
finalizacion()
