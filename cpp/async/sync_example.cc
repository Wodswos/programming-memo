#include <iostream>
#include <fstream>
#include <chrono>

void readFileSync() {
    std::ifstream file("large_file.txt");
    std::string content;
    if (file.is_open()) {
        std::getline(file, content); // 读取文件
        // std::cout << "Read file content: " << content << std::endl;
    }
}

int main() {
    auto start = std::chrono::high_resolution_clock::now();
    readFileSync();
    auto end = std::chrono::high_resolution_clock::now();
    std::cout << "Time taken: " << std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count() << " ms" << std::endl;
    return 0;
}