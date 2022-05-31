#include <iostream>

bool canSum(int targetSum, int numbers[], int lenArray)
{
    if (targetSum == 0) return true;
    if (targetSum < 0) return false;

    for (int i = 0; i < lenArray; i++)
    {
        int remainder = targetSum - numbers[i];
        if (canSum(remainder, numbers, lenArray) == true)
        {
            return true;
        }
    }

    return false;
}



int main()
{
    int numbers[] = {2, 3};
    std::cout << canSum(7, numbers, 2) << std::endl;    // true

    int numbers2[] = {5, 3, 4, 7};
    std::cout << canSum(7, numbers2, 4) << std::endl;   // true

    int numbers3[] = {2,4};
    std::cout << canSum(7, numbers3, 2) << std::endl;   // false

    int numbers4[] = {2, 3, 5};
    std::cout << canSum(8, numbers4, 3) << std::endl;   // true

    // The following will take long 
    // int numbers5[] = {7, 14};
    // std::cout << canSum(300, numbers5, 2) << std::endl; // false

    return 0;
}