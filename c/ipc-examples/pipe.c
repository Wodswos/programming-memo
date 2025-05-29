#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <sys/wait.h>

int main(){
    int fd[2];
    char buffer[100];
    const char *msg = "Hello from parent!";

    if (pipe(fd) == -1){
        perror("pipe");
        return 1;
    }

    pid_t pid = fork();
    if (pid == 0){
        close(fd[1]);
        read(fd[0], buffer, sizeof(buffer));
        printf("Child received: %s \n", buffer);
        close(fd[0]);
    }else{
        close(fd[0]);
        write(fd[1], msg, strlen(msg)+1);
        close(fd[1]);
        wait(NULL);
    }
    return 0;
}