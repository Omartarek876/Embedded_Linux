#include <iostream> 

int main() {
    char ch; 
    std::cout << "Enter a character: "; 
    std::cin >> ch; 

    if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
        std::cout << "The character is a vowel." << std::endl; 
    } else {
        std::cout << "The character is a consonant." << std::endl; 
    } 
}