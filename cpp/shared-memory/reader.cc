#include <iostream>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>
#include <cstring>

int main(){
    const char* name = "/shared_memory";
    const int SIZE = 4096;

    // open shared memory object
    int shm_fd = shm_open(name, O_RDONLY, 0666);
    if (shm_fd == -1){
        std::cerr << "Failed to open shared memory." << std::endl;
        return 1;
    }

    // map
    void* ptr = mmap(0, SIZE, PROT_READ, MAP_SHARED, shm_fd, 0);
    if (ptr == MAP_FAILED){
        std::cerr << "Failed to map memory." <<std::endl;
        return 1;
    }

    // read and print
    char* data = static_cast<char*>(ptr);
    std::cout << "Read from shared memory: " << data << std::endl;

    // unmap
    if(munmap(ptr, SIZE) == -1) {
        std::cerr << "Failed to unmap." << std::endl;
        return 1;
    }

    // delete shmem object
    if (shm_unlink(name) == -1){
        std::cerr << "Failed to delete shmem." << std::endl;
        return 1;
    }

    return 0;
}