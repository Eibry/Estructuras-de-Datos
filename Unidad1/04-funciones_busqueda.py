menu = """
Programa para calcular raices cuadradas

Elige un Algoritmo de Búsqueda

1.- Enumeración Exhaustiva
2.- Aproximación de Soluciones
3.- Búsqueda Binaria

Ingrese el número de la opción a elegir: """

option = int(input(menu))

def enumeracion(objetivo):
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raíz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene raíz cuadrada exacta')

def aproximacion(objetivo):
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontró la raíz cuadrada de {objetivo}')
    else:
        print(f'La raíz cuadrada de {objetivo} es {round(respuesta, 2)}')

def busqueda(objetivo):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'La raíz cuadrada de {objetivo} es {round(respuesta, 2)}')

def message(opcion, menu):
    print(f'Elegiste el Algoritmo de {opcion}')
    objetivo = int(input("Elige un número "))
    if menu == 1:
        enumeracion(objetivo)
    elif menu == 2:
        aproximacion(objetivo)
    elif menu == 3:
        busqueda(objetivo)

if option == 1:
    message("Enumeración Exhaustiva", 1)
elif option == 2:
    message("Aproximación de Soluciones", 2)
elif option == 3:
    message("Búsqueda Binaria", 3)
else:
    print("Elige una opción correcta")