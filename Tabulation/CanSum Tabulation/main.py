
def canSum(targetSum, numbers):
    tab = [False] * (targetSum + 1)
    tab[0] = True

    for i in range(targetSum):
        if tab[i] == True:
            for j in numbers:
                if (i + j) <= targetSum:    # checking index validity
                    tab[i + j] = True

    return tab[targetSum]


if __name__ == "__main__":
    print(canSum(7, [2, 3]))    # True
    print(canSum(7, [5, 3, 4, 7]))    # True
    print(canSum(7, [2, 4]))    # False
    print(canSum(8, [2, 3, 5]))    # True
    print(canSum(300, [7, 14]))    # False
    # print(canSum(10, [3]))