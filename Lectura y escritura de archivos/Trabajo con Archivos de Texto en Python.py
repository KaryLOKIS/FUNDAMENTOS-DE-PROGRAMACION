#semana 16
print("Trabajo con archivos de Texto en Python")

#definimos el nombre del archivo
file_name="my_notes.txt"

#modo de apertura:"r" para la lectura(read)
#procedemos abrir el archivo que creamos con el nombre my notes
archivo=open(file_name,"w")
#escribimos algunas lineas personales
archivo.write('linea 1:Me llamo Karina\n')
archivo.write('linea 2:Estudio en la Universidad Estatal Amazonica\n')
archivo.write('linea 3:En mis tiempos libres me gusta salir a pasear para distraerme\n')

#cerramos el archivo
archivo.close()
#Modo de apertura "r" para lectura(read)
archivo_lectura=open(file_name,"r")
#Metodo read(): lee el contenido del archivo
contenido_completo=archivo_lectura.read()
print("contenido completo usando read():")
print(contenido_completo)
archivo_lectura=open(file_name,"r")

contenido_completo=archivo_lectura.read()
print("contenido completo usando read():")
print(contenido_completo)
#Metodo readline():lee una linea a la vez
archivo_lectura.seek(0)
linea_1 = archivo_lectura.readline()
linea_2 = archivo_lectura.readline()
linea_3 = archivo_lectura.readline()
#metodo readlinea lee linea por linea
print("\nContendio linea por linea usando readline():")
print(linea_1.strip())
print(linea_2.strip())
print(linea_3.strip())
#cerramos el archivo my_notes
archivo_lectura.close()




