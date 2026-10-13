#include <stdio.h>

int main() {
    float num1, num2, suma;

    printf("Ingresa el primer numero: ");
    scanf("%f", &num1);

    printf("Ingresa el segundo numero: ");
    scanf("%f", &num2);

    suma = num1 + num2;

    printf("La suma es: %.2f\n", suma);

    return 0;
}