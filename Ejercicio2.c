#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid;
    // creamos la ramificacion
    pid = fork();

    if (pid == 0) {
        // Proceso hijo
        printf("Soy el proceso hijo \n");
    } else if (pid > 0) {
        // Proceso padre
        printf("Soy el proceso padre\n");
    } else {
        // si el valor es negativo, hubo un error
        printf("Error al crear el proceso hijo\n");
        return 1;
    }
    return 0;
}