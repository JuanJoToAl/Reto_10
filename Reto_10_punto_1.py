# Se declara una lista vacía para almacenar números reales 
lista_numeros: list = []

# Se declara una variable para almacenar un número real 
numero: float

# Se declara una variable booleana para controlar el bucle 
bandera: bool = True

# Bucle principal para ingresar números 
while bandera:
    try:
        # Solicitar entrada al usuario 
        numero = input("Ingrese un número real o 'Parar' para salir: ")

        # Verificar si se ingresa 'Parar' para terminar el bucle 
        if numero == "Parar":
            bandera = False

        # Si no se ingresa 'Parar', convertir a float y agregar a la lista 
        else:
            lista_numeros.append(float(numero))

    # Capturar error ValueError si se ingresa un valor no válido 
    except ValueError:
        print("Entrada inválida. Intente de nuevo.") 

# Imprimir la lista de números ingresados 
print(f"Números ingresados: {lista_numeros}")

# Calcular y mostrar el promedio de los números 
promedio_lista = sum(lista_numeros) / len(lista_numeros)
print(f"Promedio de los números: {promedio_lista}")