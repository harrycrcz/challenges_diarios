// Escribir un programa que pida al usuario dos números y los sume.¡Pero esta vez hazlo en C++!:)
#include <iostream>

int main()
{
    // Declaramos las variables a usar
    int numero1, numero2, suma;

    // Asignar valores a las variables
    numero1 = 25;
    numero2 = 70;

    // Sumamos las variables
    suma = numero1 + numero2;

    // Imprimimos el resultado
    std::cout << "La suma de " << numero1 << " y " << numero2 << " es " << suma << std::endl;

    // Esperamos a que el usuario presione una tecla antes de salir (si no hago esto, el programa se cierra muy rapido)
    std::cout << "Presiona Enter para salir...";
    std::cin.get();

    // Indicamos que el programa se cerro correctamente
    return 0;
}
