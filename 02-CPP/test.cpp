// #include <iostream> 
// /* 
//  ctrl + shift + b to build
//  ctrl + shift + c to run 
//  ctrl + shift + a to show refefences after click on what i want to navigate to its references  
//  ctrl + shift + d to show definition 
//  ctrl + shift + o to show sembols 
//  */
// int main() {
//     std::cout << "Hello, World!" << std::endl; 
//     int x = 5; 
//     if (x == 5) {
//         std::cout << "x is 5" << std::endl; 
//     } else {
//         std::cout << "x is not 5" << std::endl; 
//     }
//     return 0;
// } 

#include <iostream>

int main() {
    int num = 255;
    
    std::cout << "Decimal: " << num << std::endl;
    std::cout << "Hexadecimal: " << std::hex << num << std::endl;  // Outputs ff
    
    return 0;
}
