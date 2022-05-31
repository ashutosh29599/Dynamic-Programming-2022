#include <iostream>

const int MAXLENGTH = 100;
int memo[MAXLENGTH] = {0};

void init_memo()
{
    for (int i = 0; i < MAXLENGTH; i++)
    {
        memo[i] = -1;
    }
    // for (int i = 0; i < MAXLENGTH; i++)
    // {
    //     std::cout << memo[i] << std::endl;
    // }
}

bool canSum(int targetSum, int numbers[], int lenArray)
{
    if (targetSum == 0) return true;
    if (targetSum < 0) return false;
    if (memo[targetSum] != -1) return memo[targetSum];

    for (int i = 0; i < lenArray; i++)
    {
        int remainder = targetSum - numbers[i];
        if (canSum(remainder, numbers, lenArray) == true)
        {
            memo[targetSum] = true;
            return true;
        }
    }

    memo[targetSum] = false;
    return false;
}



int main()
{
    init_memo();
    int numbers[] = {2, 3};
    std::cout << canSum(7, numbers, 2) << std::endl;    // true

    init_memo();
    int numbers2[] = {5, 3, 4, 7};
    std::cout << canSum(7, numbers2, 4) << std::endl;   // true

    init_memo();
    int numbers3[] = {2,4};
    std::cout << canSum(7, numbers3, 2) << std::endl;   // false

    init_memo();
    int numbers4[] = {2, 3, 5};
    std::cout << canSum(8, numbers4, 3) << std::endl;   // true

    // // The following will take long 
    init_memo();
    int numbers5[] = {7, 14};
    std::cout << canSum(300, numbers5, 2) << std::endl; // false

    init_memo();
    int numbers6[] = {7, 14};
    std::cout << canSum(28, numbers6, 2) << std::endl; // false

    return 0;
}