# Búsqueda en Arreglo Multidimensional - Ejercicio 1
# matriz de 3 * 3
from types import new_class
#Creamos una matriz de 3*3 y agregamos los datos
matriz = [
    [7, 9, 3],
    [2, 4, 6],
    [1, 8, 4]
]
#Recorre cada elemento de la matriz y compara si es igual al valor buscado.
print(matriz)
# funcion de buscar el valor Especifico

def buscar_valor(matriz,valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == valor_buscado:
                return i,j
#Se imprime un mensaje indicando si el valor se encontró o no,y la posición en la matriz.

valor_buscado= 4
print(buscar_valor(matriz,valor_buscado))
if valor_buscado==4:
    print("Valor encontrado en la posicion ",buscar_valor(matriz,valor_buscado))
else:
    print("Valor invalido")




