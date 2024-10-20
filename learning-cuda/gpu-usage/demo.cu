// #include <stdio.h>
// #include <unistd.h>
// #include <stdlib.h>

// const long long tdelay=1000000LL;
// const int loops = 10000;
// const int hdelay = 1;

// __global__ void dkern(){

//     long long start = clock64();
//     while(clock64() < start+tdelay);
// }

// int main(int argc, char *argv[]){

//     int my_delay = hdelay;
//     if (argc > 1) my_delay = atoi(argv[1]);
//     for (int i = 0; i<loops; i++){
//         dkern<<<1,1>>>();
//         usleep(my_delay);}

//     return 0;
// }

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

const long long tdelay = 1000000LL;
const int loops = 10000;
const int hdelay = 1;

__global__ void dkern() {
    long long start = clock64();
    while (clock64() < start + tdelay);
}

int main(int argc, char *argv[]) {
    int my_delay = hdelay;
    if (argc > 1) {
        char *endptr;
        long val = strtol(argv[1], &endptr, 10);
        if (*endptr != '\0' || val < 0) {
            fprintf(stderr, "Invalid delay value\n");
            return 1;
        }
        my_delay = (int)val;
    }

    for (int i = 0; i < loops; i++) {
        dkern<<<1, 1>>>();
        cudaDeviceSynchronize(); // Ensure the kernel execution is complete
        usleep(my_delay);
    }

    return 0;
}