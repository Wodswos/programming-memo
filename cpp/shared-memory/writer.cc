// #include <sys/stat.h>
#include <iostream>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>
#include <cstring>

int main(){
    const char* name = "/shared_memory";
    const int SIZE = 4096;
    const char * message = "Hello, Shared Memory, this is writer!";

    // create memory object
    int shm_fd = shm_open(name, O_CREAT | O_RDWR, 06666);
    if (shm_fd == -1){
        std::cerr << "Failed to create memory size." << std::endl;
        return 1;
    }

    // set memory Size
    if (ftruncate(shm_fd, SIZE) == -1){
        std::cerr << "Failed to set memory size." << std::endl;
        return 1;
    }

    // map shmem to process address space
    void* ptr = mmap(0, SIZE, PROT_WRITE, MAP_SHARED, shm_fd, 0);
    if (ptr == MAP_FAILED){
        std::cerr << "Failed to map memory." << std::endl;
        return 1;
    }

    // write data into shared memory
    memcpy(ptr, message, strlen(message)+1);

    // unmap
    if (munmap(ptr, SIZE) == -1){
        std::cerr << "Failed to unmap." << std::endl;
    }

    // close fd
    if (close(shm_fd) == -1) {
        std::cerr << "Failed to close fd." << std::endl;
    }

    std::cout << "Data writed." << std::endl;
    return 0;
}