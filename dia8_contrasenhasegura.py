# Generador de Contraseñas Seguras: Escribe un programa que genere
# una contraseña segura de longitud variable (entre 8 y 16 caracteres) que incluya letras mayúsculas, minúsculas, números y símbolos.

# Paso 1. Importamos las librerias necesarias, 'random' para generar el password de manera aleatoria y 'string' para proveernos
# con los strings necesarios en mayusculas, minusculas, numeros y simbolos
import random
import string

# Paso 2. Definimos la funcion generadora.


def password_generador():
    # Definimos los componentes necesarios pa la contrasenha:
    minuscula = string.ascii_lowercase
    mayuscula = string.ascii_uppercase
    numerito = string.digits
    simbolo = string.punctuation
    # Nos aseguramos de que la contrasenha incluya si o si todos estos elementos.
    caracteres_necesarios = minuscula + mayuscula + numerito + simbolo
    # Le damos los caracteres necesarios a la nueva contrasenha
    nueva_contrasenha = [random.choice(minuscula), random.choice(mayuscula),
                         random.choice(numerito), random.choice(simbolo)]
    # Asignamos una longitud random entre 8 y 16 a la contrasenha (nos devolvera un entero)
    longitud_contrasenha = random.randint(8, 16)
    # Agregamos nuevos caracteres a la contrasenha (a la longitud de la contrasenha la decrecemos entre 4 porque la contrasenha
    # ya tiene los 4 caracteres necesarios, asi que de no hacer la resta, podria llegar a tener 20 caracteres)
    nueva_contrasenha += random.choices(caracteres_necesarios,
                                        k=longitud_contrasenha-4)
    # Mezclamos la contrasenha.
    random.shuffle(nueva_contrasenha)
    # Retornamos la nueva contrasenha como un str
    return ''.join(nueva_contrasenha)


# Llamamos a la funcion imprimiendo la nueva contrasenha
print(password_generador())
