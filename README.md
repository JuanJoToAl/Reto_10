# Reto 10
_El siguiente repositorio muestra las soluciones a los puntos del reto 10_

### 1. Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

```python
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
```

### 2. Desarrollar un algoritmo que calcule el [producto punto](https://www.cuemath.com/algebra/dot-product/) de dos arreglos de números enteros (reales) de igual tamaño.

```python
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
```

### 3. Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.

```python
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
```

### 4. Revisar que son los algoritmos de *sorting*, entender *bubble-sort* ([enlace](https://www.geeksforgeeks.org/bubble-sort/) a implementación).

Para este punto no se tuvo que realizar un código propiamente, pero se realizó la investigación sobre qué son los algoritmos de sorting.
