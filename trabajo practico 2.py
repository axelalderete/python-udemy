import time
import random
import string
def inicio():
    print("modo carga")
    print("1 = automatico")
    print("2 = manual")
    opcion = int(input("ingrese modo de carga:"))
    return opcion


def menu():
    opcion = inicio()
    timeout = time.time() + 60*2   # 4 minutes from now
    listaTickets = []
    if opcion == 2:

        while time.time() < timeout:
            ticket = cargaManual(timeout)
            listaTickets.append(ticket)
    else:
        while time.time() < timeout:
            ticket = cargaAutomatica(timeout)
            listaTickets.append(ticket)

    calculos(listaTickets)

def cargaManual(timeout):
    tipoVehiculo = int(input("ingrese tipo de vehiculo :"))
    formaDePago = int(input("ingrese forma de pago :"))
    if formaDePago == 2:
        patente = input("ingrese la patente :")
    else:
        patente = ""
    ticket = (tipoVehiculo , formaDePago, patente, timeout-time.time())
    return ticket

def cargaAutomatica(timeout):
    time.sleep(random.randint(1, 2)) # Delays for 10 seconds.
    tipoVehiculo = random.randint(1, 3)
    formaDePago = random.randint(1, 2)
    if formaDePago == 2:
        numeros = random.randint(100,999)
        letra1 = random.choice(string.ascii_lowercase)
        letra2 = random.choice(string.ascii_lowercase)
        letra3 = random.choice(string.ascii_lowercase)
        patente = str(numeros) + letra1 + letra2 + letra3
    else:
        patente = ""
    ticket = (tipoVehiculo , formaDePago, patente, timeout-time.time())
    return ticket

def calculos(lista):
    ingresoHora1 = 0
    ingresoHora2 = 0
    ingresoHora3 = 0
    ingresoHora4 = 0
    tiempo = 0
    patente = " "
    cantidadPasadasEfectivo = 0
    cantidadPasadasTelepeaje = 0
    cantidadAutos = 0
    cantidadMotos = 0
    cantidadcamiones = 0
    totalEfectivo = 0
    totalTelepeaje = 0
    for x in lista:
        if x[3] < 60:
            ingresoHora1 += 1
        if 60 > x < 120:
            ingresoHora2 += 1
        if 120 < x < 180:
            ingresoHora3 += 1
        else:
            ingresoHora4 += 1
        if x[2] > patente :
            patente = x[2]
            tiempo = x[3]

        if x[0] == 2 :
            cantidadAutos += 1
            if x[1] == 1:
                totalEfectivo += 40
                cantidadPasadasEfectivo += 1
            else:
                totalTelepeaje += 40
                cantidadPasadasTelepeaje += 1
        elif x[1] == 1 :
            cantidadMotos += 1
            if x[1] == 1:
                totalEfectivo += 20
                cantidadPasadasEfectivo += 1
            else:
                totalTelepeaje += 20
                cantidadPasadasTelepeaje += 1
        else:
            cantidadcamiones += 1
            if x[1] == 1:
                totalEfectivo += 80
                cantidadPasadasEfectivo += 1
            else:
                totalTelepeaje += 80
                cantidadPasadasTelepeaje += 1

    print("la cantidad de autos es:" ,cantidadAutos)
    print("cantidad de motos:" ,cantidadMotos)
    print("cantidad de camiones:" ,cantidadcamiones)
    print("total recaudado en efectivo" ,totalEfectivo)
    print("total recaudado con telepeaje" ,totalTelepeaje)
    print("cantidad total de pases " + str(len(lista)))
    print("cantidad promedio: " + str(len(lista)/4))
    if cantidadPasadasTelepeaje > cantidadPasadasEfectivo:
        print("mayor cantidad de pasadas telepeaje")
    else:
        print("mayor cantidad de pasadas efectivo")
    print("la patente mas nueva es:" ,patente)
    print("el tiempo en el que ingreso esta patente:" ,tiempo)
    if ingresoHora1 > ingresoHora2 and ingresoHora1 > ingresoHora3 and ingresoHora1 > ingresoHora4:
        print("hubo mas ingreso en la hora 1 con" ,ingresoHora1 )
    if ingresoHora2 > ingresoHora1 and ingresoHora2 > ingresoHora3 and ingresoHora2 > ingresoHora4:
        print("hubo mas ingreso en la hora 2" ,ingresoHora2)
    if ingresoHora3 > ingresoHora2 and ingresoHora3 > ingresoHora1 and ingresoHora3 > ingresoHora4:
        print("hubo mas ingreso en la hora 3" ,ingresoHora3)
    if ingresoHora4 > ingresoHora2 and ingresoHora4 > ingresoHora3 and ingresoHora4 > ingresoHora1:
        print("hubo mas ingreso en la hora 4" ,ingresoHora4)





menu()

