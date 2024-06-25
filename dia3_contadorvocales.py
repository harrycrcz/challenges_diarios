# Contar Vocales: Escribe un programa que cuente el número de vocales en una cadena dada.

# Hacer la cadena de texto
perro = 'Es un canino'

# Hacer una lista con las vocales existentes
vocales = ['a', 'e', 'i', 'o', 'u']

contador_vocales = 0
for i in perro:
    i = i.lower()
    if i in vocales:
        contador_vocales += 1


print(f'La frase tiene {contador_vocales} vocales')
