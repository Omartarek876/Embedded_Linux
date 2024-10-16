// #include <iostream>

// int main() {
//     int num, remainder;
//     int res = 0, c = 1;  // Initialize res as 0 and c as 1 (to build binary result)

//     std::cout << "Enter any number: ";
//     std::cin >> num;

//     while (num != 0) {
//         remainder = num % 2;  // Get the current binary digit (0 or 1)
//         res += remainder * c;  // Build the binary number
//         c *= 10;               // Move to the next place in the binary result
//         num /= 2;              // Update the number by dividing it by 2
//     }

//     std::cout << "Binary: " << res << std::endl;

//     return 0;
// }


#include <iostream>
#include <bitset>

int main() {
    int decimalNumber;
    
    // Input a decimal number
    std::cout << "Enter a decimal number: ";
    std::cin >> decimalNumber;
    
    // Assuming 32 bits for the binary representation
    std::bitset<32> binary(decimalNumber);

    // Output the binary representation
    std::cout << "Binary representation: " << binary << std::endl;

    return 0;
}
