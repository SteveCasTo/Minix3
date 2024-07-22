// Ejercicio 3: Crear múltiples procesos hijos y que cada uno imprima su PID.

#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    int num_procs = 5;  // Número de procesos hijos a crear
    int i;

    for (i = 0; i < num_procs; i++) {
        pid_t pid = fork();

        if (pid == 0) {
            // Proceso hijo
            printf("Soy el proceso hijo %d con PID: %d\n", i+1, getpid());
            return 0;
        } else if (pid < 0) {
            printf("Error al crear el proceso hijo\n");
            return 1;
        }
    }

    // Proceso padre
    for (i = 0; i < num_procs; i++) {
        wait(NULL);  // Esperar a que cada hijo termine
    }

    return 0;
}