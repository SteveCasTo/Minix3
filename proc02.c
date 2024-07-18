#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main() {
    int pipefd[2];
    pid_t pid;
    const char *message = "Hola desde el proceso padre!";
    char buffer[128];

    // Crear la tubería
    if (pipe(pipefd) == -1) {
        perror("Error al crear la tubería");
        exit(EXIT_FAILURE);
    }

    // Crear el proceso hijo
    pid = fork();
    if (pid < 0) {
        perror("Error al crear el proceso hijo");
        exit(EXIT_FAILURE);
    } else if (pid == 0) {
        // Este es el proceso hijo
        close(pipefd[1]); // Cerrar el extremo de escritura de la tubería
        read(pipefd[0], buffer, sizeof(buffer));
        close(pipefd[0]); // Cerrar el extremo de lectura de la tubería
        printf("Proceso hijo recibió el mensaje: %s\n", buffer);
        exit(EXIT_SUCCESS);
    } else {
        // Este es el proceso padre
        close(pipefd[0]); // Cerrar el extremo de lectura de la tubería
        write(pipefd[1], message, strlen(message) + 1);
        close(pipefd[1]); // Cerrar el extremo de escritura de la tubería
        wait(NULL); // Esperar a que el hijo termine
    }

    return 0;
}

