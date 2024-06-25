# DIA 4
# Ordenar Lista:
# Escribe un programa que ordene una lista de números dada por el usuario en orden ascendente.


lista_numeros = []
tamanho_lista = int(input('Dime cuantos numeros vas a introducir'))

if tamanho_lista < 10:
    for numero in range(tamanho_lista):
        numero = int(input('Decime un numero'))
        lista_numeros.append(numero)
    lista_numeros.sort()
print(lista_numeros)
