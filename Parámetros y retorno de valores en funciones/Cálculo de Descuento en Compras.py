print("Semana 14")
print("***** Parámetros y Retorno de Valores en Funciones *****")

# vamos a repasar la clase de la semana 14 parametros y retorno de valores
def saludar(nombre, edad):
    print(f"Hola, {nombre} tienes {edad} años.")
# Llamada a la función y paso de argumentos
saludar("Karina", 28)
# funcion con Parámetros predeterminados
def saludar_con_saludo(nombre, edad, saludo="Hola Buenos Dias"):
    print(f"{saludo}, {nombre} tienes {edad} años.")
# Llamamos a la funcion e imprimimos
saludar_con_saludo("Jessica", 32, "¡Hola!")

# Tarea Semana 14:  Descuentos a los montos de compra
print("**** Total de Compras más Descuentos ****")
# funcion para crear el descuento de compra
def calcular_descuento(valor_total, porcentaje_descuento=15):
    descuento = valor_total * porcentaje_descuento / 100
    return descuento

monto_total1=1000
# Llamada a la función
descuento1 = calcular_descuento(monto_total1)
print(f"El monto total es:",monto_total1)
print(f'El valor del descuento es:', descuento1)
#monto total y procenataje de la compra
monto_total2=2000
porcentaje_descuento=15
descuento2 = calcular_descuento(2000, porcentaje_descuento=15)
#imprimimos los montos totales y los descuentos respectivos
print("El monto es:", monto_total2)
print(f"El valor del descuento es:", descuento2)

