#include <iostream> 

int main() {
    int num1, num2 , num3;  
    
    std::cout << "Enter three numbers: "; 
    std::cin >> num1 >> num2 >> num3; 

    std::cout << "The maximum number is: " << std::max(std::max(num1, num2), num3) << std::endl;
}