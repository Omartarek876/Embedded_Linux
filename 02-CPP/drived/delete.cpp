#include <iostream>
#include <vector>
#include <algorithm> // Include this header for std::remove

void deleteNumber(std::vector<int>& arr, int x) {
    // Use the erase-remove idiom to remove the specified number
    arr.erase(std::remove(arr.begin(), arr.end(), x), arr.end());
}

int main() {
    std::vector<int> arr = {1, 2, 3, 4, 5, 3, 6, 7, 3, 8}; // Example array with duplicates
    int x;

    std::cout << "Original array: ";
    for (int num : arr) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    std::cout << "Enter a number to delete: ";
    std::cin >> x;

    deleteNumber(arr, x);

    std::cout << "Array after deletion: ";
    for (int num : arr) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
