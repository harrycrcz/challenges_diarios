def inversor_cadena(cadena, n, nueva_cadena):
    if nueva_cadena == ' ':
        nueva_cadena = []
    nueva_cadena.append(cadena[n])
    if n >= 1:
        inversor_cadena(cadena, n-1, nueva_cadena)
    return nueva_cadena


cadena_caracteres = ['r', 'a', 't', 'a', 'm',
                     ' ', 'e', 'd', ' ', 'o', 'r', 'u', 'D']
print(inversor_cadena(cadena_caracteres, 12, ' '))
