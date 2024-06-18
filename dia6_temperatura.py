# Conversión de Temperatura: Escribe un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit.

# Paso 1. Damos una temperatura en Celsius.
temperatura = 39

# Paso 2. definimos una funcion con la formula para convertir grados Celsius a Fahrenheit y retornar.


def conversor_temp(temp_celsius):
    temp_fahrenheit = (temp_celsius*9/5) + 32
    return temp_fahrenheit


# Paso 3. Imprimir la temperatura en grados Fahrenheit.
print(conversor_temp(temperatura))
