#include <iostream>
#include <thread>
#include <atomic>

using namespace std;

int main(int argc, char* argv[]){
    atomic<int> sum= 0;

    auto f = [&sum](){
        for(int i = 0; i <1000000; i++) {
            // sum += 1 & sum ++ 这类运算是原子性的
            // sum = sum + 1 不是原子性的，需要额外的保护
            sum+= 1;
        }
    };

    thread t1(f);
    thread t2(f);

    t1.join();
    t2.join();

    cout << sum <<endl;

    return 0;
}