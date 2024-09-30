#include <iostream>

int main() {
    int num, remainder;
    int res = 0, c = 1;  // Initialize res as 0 and c as 1 (to build binary result)

    std::cout << "Enter any number: ";
    std::cin >> num;

    while (num != 0) {
        remainder = num % 2;  // Get the current binary digit (0 or 1)
        res += remainder * c;  // Build the binary number
        c *= 10;               // Move to the next place in the binary result
        num /= 2;              // Update the number by dividing it by 2
    }

    std::cout << "Binary: " << res << std::endl;

    return 0;
}
