#Ordenación de Arreglo Multidimensional - Ejercicio 2
#Creacion de la matriz
matriz = [
    [1, 6, 51],
    [48, 28, 75],
    [31, 9, 100]
]
# Verificamos si se impreme nuestra matriz
print(matriz)

#Utilizare la funcion especifica usando Bubble Sort
#Nos ayudara a ordenar nuestra matriz en linea

#Ejecutamos el programa

def buble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(n-1, i, -1):
            if fila[j] > fila[j-1]:
                fila[j], fila[j-1] = fila[j-1], fila[j]

#Muestra la matriz ordenada en linea
                print(fila)
#Ordenaremos de mayor a menor [2]
#Tendremos la matriz original y la ordenada
print("Matriz Original")
print(matriz)
buble_sort(matriz[2])
print(matriz)

