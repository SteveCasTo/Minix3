// Ejercicio 5: Implementar un sistema básico de concurrencia usando fork().
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

void proceso_hijo(int num) {
    printf("Soy el proceso hijo %d con PID: %d\n", num, getpid());
    sleep(1);  // Simular trabajo en el proceso hijo
    printf("Proceso hijo %d terminado.\n", num);
}

int main() {
    int num_procs = 5;  // Número de procesos hijos a crear
    int i;

    for (i = 0; i < num_procs; i++) {
        pid_t pid = fork();

        if (pid == 0) {
            // Proceso hijo
            proceso_hijo(i + 1);
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