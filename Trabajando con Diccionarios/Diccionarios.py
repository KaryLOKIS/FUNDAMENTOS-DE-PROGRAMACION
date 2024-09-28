print("SEMANA 15")
print("TRABAJANDO CON DICCIONARIOS")
#Comenzaremos creando un diccionario con informacion personal
informacion_personal={
    "nombre":"Victor",
    "apellido":"Gonzales",
    "edad": 27,
    "ciudad":"Esmeralda",
}
#acceder y mmodificar valores

# obtenemos los valores
print("nombre: ",informacion_personal["nombre"])
print("apellido:",informacion_personal["apellido"])
print("edad:",informacion_personal["edad"])
print("ciudad:",informacion_personal["ciudad"])
#Acceder y Modificar Valores:

# Modificacion de la ciudad
informacion_personal["ciudad"] = "Quito"  # Cambiamos "Esmeralda" por "Quito"
# Imprimimos los valores después de cambiar la ciudad
print("Ciudad modificada:", informacion_personal["ciudad"])

#Agregamos una nueva clave-valor al diccionario que seria en este caso la profesion
informacion_personal["Profesion"]="Ingeniero en Sistemas"
#Imprimimos la nueva clave que es la profesion
print("Profesion",informacion_personal["Profesion"])

#Verificar Existencia de Claves:

#Agregamos la clave de "telefono"
informacion_personal["Telefono"]="0998528081"
#Imprimimos nuestra nueva clave que es telefono
print("Telefono",informacion_personal["Telefono"])

#Eliminar una Clave:

#Eliminaremos la clave "edad"
del informacion_personal["edad"]
#Imprimimos el resultado sin el valor de edad
print("todo:",informacion_personal)

print("***** Impresion del Diccionario Final *****")
#Imprimir el Diccionario Final: con todos las operaciones realizadas
#recorrer con un for
for clave,valor in informacion_personal.items():
     print(clave,":",valor)




