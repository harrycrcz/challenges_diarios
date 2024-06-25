# - Tabla de Multiplicar:
# Escribe un programa que muestre la tabla de multiplicar de un número dado por el usuario.

def tabla_multiplicar(numero):
    numero = int(input('Dame un numerito por favor'))
    tabla = []
    for i in range(11):
        if i == 0:
            tabla = []
        else:
            tabla.append(f'{i} x {numero} = {numero*i}')
    print(tabla)


tabla_multiplicar(4)
