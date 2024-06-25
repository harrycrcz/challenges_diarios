#include <iostream>
#include <algorithm> // Para std::sort

int main()
{
    // Definir un array de enteros
    int arr[] = {5, 2, 9, 1, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]); // Calcular el tamaño del array

    // Imprimir el array antes de ordenar
    std::cout << "Array antes de ordenar: ";
    for (int i = 0; i < n; ++i)
    {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    // Ordenar el array de menor a mayor usando el sort
    std::sort(arr, arr + n);

    // Imprimir el array después de ordenar
    std::cout << "Array después de ordenar: ";
    for (int i = 0; i < n; ++i)
    {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
