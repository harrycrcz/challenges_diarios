# Juego de Piedra, Papel o Tijeras: Escribe un programa que permita al usuario jugar piedra, papel o tijeras contra la computadora.

# Paso 1. Importamos 'random', que nos servira para asignar jugadas aleatorias a la maquina.
import random
# Paso 1. Definimos variables para piedra, papel o tijera.
piedra = 'piedra'
papel = 'papel'
tijera = 'tijera'

# Paso 2. Definimos la funcion que nos permitira jugar


def jugada():
    turno_jugador = input('Diga su jugada').lower()

    opciones = [piedra, papel, tijera]
    turno_maquina = random.choice(opciones)
    print(f'La maquina ha jugado {turno_maquina}')
    # Definimos las posibles combinaciones:
    if turno_jugador == turno_maquina:
        print('Jugada empatada')
        return 0
    elif turno_jugador == piedra and turno_maquina == tijera or\
            turno_jugador == papel and turno_maquina == piedra or\
            turno_jugador == tijera and turno_maquina == papel:
        print('Has ganado este turno')
        return 1
    elif turno_jugador == piedra and turno_maquina == papel or\
            turno_jugador == papel and turno_maquina == tijera or\
            turno_jugador == tijera and turno_maquina == piedra:
        print('Has perdido este turno')
        return -1

# Paso 3. Definimos la funcion que acumulara los puntajes y nos dira quien gana


def hakembo():
    puntos_jugador = 0
    puntos_maquina = 0
    while puntos_jugador < 2 and puntos_maquina < 2:
        resultado = jugada()
        if resultado == 1:
            puntos_jugador += 1
        elif resultado == -1:
            puntos_maquina += 1
        print(f'''Marcador: Jugador: {
              puntos_jugador}. Maquina: {puntos_maquina}''')

    if puntos_jugador == 2:
        print('Has ganado la partida')
    else:
        print('La computadora ha ganado')


hakembo()
