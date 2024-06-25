// Palíndromo: Escribir un programa que determine si una cadena de caracteres ingresada por el usuario es un palíndromo ¡Pero hazlo en C++! :)
#include <iostream>
#include <string>
#include <cctype> // Para std::tolower

bool es_palindromo(const std::string &str)
{
    std::string cleaned_str;
    // Copiar la cadena original a cleaned_str
    for (char c : str)
    {
        if (std::isalnum(c))
        {                                           // Solo agregar caracteres alfanuméricos
            cleaned_str.push_back(std::tolower(c)); // Convertir a minúsculas para evitar errores.
        }
    }

    // Comparar la cadena original con su versión invertida
    return cleaned_str == std::string(cleaned_str.rbegin(), cleaned_str.rend());
}
// Pedimos al usuario que ingrese la cadena de texto
int main()
{
    std::string cadena;
    std::cout << "Ingrese una cadena: ";
    std::getline(std::cin, cadena);

    if (es_palindromo(cadena))
    {
        std::cout << "La cadena ingresada es un palindromo.\n";
    }
    else
    {
        std::cout << "La cadena ingresada NO es un palindromo.\n";
    }

    return 0;
}
