# Inicialización de listas para almacenar números y ceros
lista_numeros: list = []  
lista_ceros: list = []    

# Variable para almacenar número ingresado por el usuario
numero: str

# Bandera para controlar el bucle
bandera: bool = True

# Bucle para ingresar números o detenerse con "Parar"
while bandera:
    try:
        numero = str(input("Ingrese un número real o 'Parar' para dejar de agregar"))
        if numero == "Parar":
            bandera = False
        else:
            # Se llena la lista_numeros con valores ingresados por el usuario
            lista_numeros.append(float(numero))
    except ValueError:
        print("Los caracteres ingresados no son válidos, intente de nuevo")

# Contar la cantidad de ceros en la lista
print(f"La lista tiene {lista_numeros.count(0)} cero(s): {lista_numeros}")

# Se crea una lista con los números oero sin los ceros
lista_ceros = [n for n in lista_numeros if n != 0]

# Añadir ceros al final de la lista si es necesario
while len(lista_ceros) != len(lista_numeros):
    lista_ceros.append(0)

# Se mmuestra la lista ordenada con ceros al final
print(f"La lista ordenada con el o los ceros al final es: {lista_ceros}")
