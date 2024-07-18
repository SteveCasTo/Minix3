#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(){
	pid_t pid;
	pid = fork();
	if (pid < 0){
		printf("Error en la creacion \n");
	}
	else if (pid == 0){
		printf("Proceso hijo id: %d \n", getpid());
		execl("/bin/ls", "ls", NULL);
		perror("proceso ha fallado");	
	}
	else{
		printf("So el proceso padre con id: %d \n", getpid());
		int estado;
		waitpid(pid, &estado, 0);
		if (WIFEXITED(estado)){
			printf("proceso hijo termino, velo a estado listos");
			printf("hijo concluyo con estado: %d \n", WEXITSTATUS(estado));
		}
	}
	return 0;
} 

