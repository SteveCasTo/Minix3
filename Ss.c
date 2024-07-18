#include <sys/wait.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
    pid_t pid1, pid2; 
    int status;

    pid1 = fork();
    if (pid1 == 0) {
        sleep(5);
        exit(5);
    } else if (pid1 < 0) {
        perror("fork");
        exit(1);
    }

    pid2 = fork();
    if (pid2 == 0) {
        sleep(1);
        exit(1);
    } else if (pid2 < 0) {
        perror("fork");
        exit(1);
    }

    waitpid(pid1, &status, 0);
    waitpid(pid2, &status, 0);

    return 0;
}
