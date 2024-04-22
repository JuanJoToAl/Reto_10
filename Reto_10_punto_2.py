# Se declaran e/o inicializan varaibles
lista1: list = []
lista2: list = []
numero1: float
numero2: float
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
    while len(lista1) < longitud_lista:
        try:
            numero1 = float(input("Ingrese un número entero para la lista 1"))
        except ValueError:
            print("Los caracteres ingresados no son válidos, intente de nuevo")
        
        # Se llena la lista1 con valores ingresados por el usuario
        lista1.append(float(numero1))
    print(f"Valores de lista1: {lista1}")

    # Se ejecuta bucle hasta longitud deseada en la lista
    while len(lista2) < longitud_lista:
        try:
            numero2 = float(input("Ingrese un número entero para la lista 2"))
        except ValueError:
            print("Los caracteres ingresados no son válidos, intente de nuevo")
        
        # Se llena la lista2 con valores ingresados por el usuario
        lista2.append(float(numero2))
    print(f"Valores de lista2: {lista2}")

    # Calcular el producto punto de las listas
    for n in lista1:
        producto_punto += lista1[indice] * lista2[indice]
        indice += 1

# Mostrar el resultado del producto punto
print(f"El producto punto de la lista1 y lista2 es: {producto_punto}")
