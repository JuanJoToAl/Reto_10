# Se declaran e/o inicializan varaibles
lista_1: list = []
lista_2: list = []
numero_1: float
numero_2: float
producto_punto: float = 0
indice: int = 0
longitud_lista: int

# Solicitar al usuario la cantidad de valores para las listas
longitud_lista = int(input("Ingrese la cantidad de valores para las listas"))

# Verificar que la longitud no sea negativa
if longitud_lista < 0:
    print("No pueden haber longitudes negativas")
    
else:
    # Se ejecuta bucle hasta longitud deseada en la lista
    while len(lista_1) < longitud_lista:
        try:
            numero_1 = float(input("Ingrese un número entero para la lista 1"))
        except ValueError:
            print("Los caracteres ingresados no son válidos, intente de nuevo")
        
        # Se llena la lista1 con valores ingresados por el usuario
        lista_1.append(float(numero_1))
    print(f"Valores de lista1: {lista_1}")

    # Se ejecuta bucle hasta longitud deseada en la lista
    while len(lista_2) < longitud_lista:
        try:
            numero_2 = float(input("Ingrese un número entero para la lista 2"))
        except ValueError:
            print("Los caracteres ingresados no son válidos, intente de nuevo")
        
        # Se llena la lista2 con valores ingresados por el usuario
        lista_2.append(float(numero_2))
    print(f"Valores de lista2: {lista_2}")

    # Calcular el producto punto de las listas
    for n in lista_1:
        producto_punto += lista_1[indice] * lista_2[indice]
        indice += 1

# Mostrar el resultado del producto punto
print(f"El producto punto de la lista1 y lista2 es: {producto_punto}")
