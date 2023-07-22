# Importamos el módulo 'random' para generar números aleatorios.

import random

# Generación de la matriz
def generar_matriz(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(random.randint(0, 9))
        matriz.append(fila)
    return matriz

# Impresión de la matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=' ')
        print()

# Cálculo de las sumas
def calcular_sumas(matriz):
    sumas_filas = []
    sumas_columnas = []
    n = len(matriz)
    for i in range(n):
        suma_fila = 0
        suma_columna = 0
        for j in range(n):
            suma_fila += matriz[i][j]
            suma_columna += matriz[j][i]
        sumas_filas.append(suma_fila)
        sumas_columnas.append(suma_columna)
    return sumas_filas, sumas_columnas

# Impresión de las sumas
def imprimir_sumas(sumas_filas, sumas_columnas):
    print("Suma de las filas:")
    for i in range(len(sumas_filas)):
        print("Fila", i + 1, ":", sumas_filas[i])

    print("\nSuma de las columnas:")
    for i in range(len(sumas_columnas)):
        print("Columna", i + 1, ":", sumas_columnas[i])

# Solicitar tamaño de la matriz
while True:
    try:
        N = int(input("Ingrese el tamaño de la matriz (N): "))
        if N <= 0:
            raise ValueError
        break
    except ValueError:
        print("Error: ¡Ingrese un número entero positivo!")

# Generar matriz y mostrarla
matriz = generar_matriz(N)
print("\nMatriz generada:")
imprimir_matriz(matriz)

# Calcular y mostrar las sumas
sumas_filas, sumas_columnas = calcular_sumas(matriz)
print("\nSumas:")
imprimir_sumas(sumas_filas, sumas_columnas)
