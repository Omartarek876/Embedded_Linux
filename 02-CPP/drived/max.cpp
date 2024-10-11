#include <iostream> 
#include <initializer_list>
#include <vector>

int max_func (std::initializer_list<int>&arr) {
    int max = 0;
    if (arr.size() == 0) {
        std::cout << "Empty array" << std::endl;
    }
    else{
    for (auto num : arr) {
        if (num > max) {
            max = num;
        }
    }
    }

    return max;
}

int main (){
    std::initializer_list<int> arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    std::cout << "Max number is: " << max_func(arr) << std::endl;
}