#include <iostream>

void GenerarPotencias(double N) {
    std::cout << "Potencias de " << N << ":" << std::endl;

    double potencia = 1.0;
    for (int i = 0; i <= 10; ++i) {
        std::cout << potencia << std::endl;
        potencia *= N;
    }
}

int main() {
    double numero;
    std::cout << "Ingrese un numero: ";
    std::cin >> numero;
    GenerarPotencias(numero);

    std::cin.ignore();  
    std::cin.get();    

    return 0;
}