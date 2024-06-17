# Crear un Diccionario: Escribe un programa que cree un diccionario a partir de dos listas dadas: una de claves y otra de valores.

# Paso 1. Crear dos listas dadas.
categoria = ['mosca', 'gallo', 'pluma', 'ligero',
             'welter', 'mediano', 'semipesado', 'pesado']
campeones = ['Pantoja', "Sean O'Malley", 'Ilia Topuria', 'Islam Makhachev',
             'Leon Edwards', 'Dricus Du Plessis', 'Alex Pereira', 'Jon Jones']

# Paso 2. Crear un diccionario vacio.
campeones_por_categoria_ufc = {}
for i in range(len(categoria)):
    campeones_por_categoria_ufc[categoria[i]] = campeones[i]


print(campeones_por_categoria_ufc)
