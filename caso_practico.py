import random

def generar_matriz(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(random.randint(0, 9))
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def calcular_sumas(matriz):
    sumas_filas = []
    sumas_columnas = []
    n = len(matriz)
    for i in range(n):
        suma_fila = sum(matriz[i])
        sumas_filas.append(suma_fila)
        
        suma_columna = 0
        for j in range(n):
            suma_columna += matriz[j][i]
        sumas_columnas.append(suma_columna)
    
    return sumas_filas, sumas_columnas

def imprimir_sumas(sumas_filas, sumas_columnas):
    print("Suma de las filas:")
    for i, suma in enumerate(sumas_filas):
        print(f"Fila {i+1}: {suma}")
    
    print("\nSuma de las columnas:")
    for i, suma in enumerate(sumas_columnas):
        print(f"Columna {i+1}: {suma}")

# Pedir al usuario el tamaño de la matriz
while True:
    try:
        N = int(input("Ingrese el tamaño de la matriz (N): "))
        if N <= 0:
            raise ValueError
        break
    except ValueError:
        print("¡Ingrese un número entero positivo!")

# Generar y mostrar la matriz
matriz = generar_matriz(N)
print("\nMatriz generada:")
imprimir_matriz(matriz)

# Calcular y mostrar las sumas
sumas_filas, sumas_columnas = calcular_sumas(matriz)
print("\nSumas:")
imprimir_sumas(sumas_filas, sumas_columnas)
