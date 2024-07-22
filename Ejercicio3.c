// Ejercicio 2: Crear un proceso hijo que calcule el factorial de un número.

#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

// funcion para computo de factorial
int factorial(int n) {
    if (n == 0 || n == 1)
        return 1;
    else
        return n * factorial(n - 1);
}

int main() {
    pid_t pid;
    int num = 5;  // Número para calcular el factorial

    // creamos otro proceso	
    pid = fork();

    if (pid == 0) {
        // Proceso hijo
        int fact = factorial(num);
        printf("Factorial de %d es %d\n", num, fact);
    } else if (pid > 0) {
        // Proceso padre
        for ( int i=0; i<100; i++){
        	printf("%d \n", i);
        }
        printf("Esperando a que el hijo termine...\n");
        wait(NULL);
        printf("Proceso hijo terminado.\n");
    } else {
        printf("Error al crear el proceso hijo\n");
        return 1;
    }

    return 0;
}
