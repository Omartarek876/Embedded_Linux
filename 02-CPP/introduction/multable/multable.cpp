#include <iostream> 

int main() {
    
    for (int i = 1; i <= 12; i++) {
        std::cout << "Multiples of " << i << ": ";
        for (int j = 1; j <= 12; j++) {
            std::cout << i * j << " " << std::endl; 
        }
        std::cout << std::endl; 
    }
}