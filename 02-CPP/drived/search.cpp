#include <iostream>
#include <initializer_list>

void search(std::initializer_list<int> arr, int x) {
    int flag = 0; // Flag to indicate if the number is found
    int index = 0; // To track the index of the current element

    if (arr.size() == 0) {
        std::cout << "Empty array" << std::endl;
    } else {
        for (auto num : arr) {
            if (num == x) { 
                flag = 1;
                std::cout << "The number exists at index " << index << std::endl; // Print the index
                break; // Exit the loop if the number is found
            }
            index++; // Increment index for the next element
        }
    }

    if (flag == 0) {
        std::cout << "The number does not exist" << std::endl;
    }
}

int main() {
    int x;
    std::cout << "Enter a number: ";
    std::cin >> x; // Removed std::endl here
    std::initializer_list<int> arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    search(arr, x); // Call the search function
    return 0; // Return 0 from main
}
