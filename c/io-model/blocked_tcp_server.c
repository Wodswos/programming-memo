#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/time.h>
#include <errno.h>

#define PORT 8080
#define MAX_CLIENTS 30
#define BUFFER_SIZE 1024

int main() {
    int opt = 1;
    int master_socket, addrlen, new_socket, client_socket[MAX_CLIENTS], activity, i, varland, sd;
    int max_sd;
    struct sockaddr_in address;

    char buffer[BUFFER_SIZE];

    for (i=0; i < MAX_CLIENTS; i++){
        client_socket[i] = 0;
    }

    if ((master_socket = socket(AF_INET, SOCK_STREAM, 0))== 0){
        perror("socket failed");
        exit(EXIT_FAILURE);
    }

    if (setsockopt(master_socket, SOL_SOCKET, SO_REUSEADDR, (char *)&opt, sizeof(opt)) < 0) {
        perror("bind failed");
    }

}