// Ejercicio 4: Crear un árbol de procesos con múltiples niveles de profundidad.
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

void crear_proceso(int level, int max_levels) {
    if (level >= max_levels)
        return;

    pid_t pid = fork();

    if (pid == 0) {
        // Proceso hijo
        printf("Soy el proceso hijo en el nivel %d con PID: %d\n", level, getpid());
        // crear el hijo del hijo
        crear_proceso(level + 1, max_levels);
        return;
    } else if (pid > 0) {
        // Proceso padre
        printf("Soy el proceso padre en el nivel %d con PID: %d\n", level, getpid());
        wait(NULL);  // Esperar a que el hijo termine
    } else {
        printf("Error al crear el proceso hijo\n");
        return;
    }
}

int main() {
    int max_levels = 3;  // Número máximo de niveles en el árbol

    crear_proceso(0, max_levels);

    return 0;
}