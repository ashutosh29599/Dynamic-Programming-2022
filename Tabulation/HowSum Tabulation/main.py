import copy

def howSum(targetSum, numbers):
    tab = [None] * (targetSum + 1)
    tab[0] = []

    for i in range(targetSum):
        if tab[i] != None:
            for num in numbers:
                if (i + num) <= targetSum:
                    tab[i + num] = copy.deepcopy(tab[i])
                    tab[i + num].append(num)

    return tab[targetSum]

if __name__ == "__main__":
    print(howSum(7, [2, 3]))    # [3, 2, 2]
    print(howSum(7, [5, 3, 4, 7]))    # [4, 3]
    print(howSum(7, [2, 4]))    # None
    print(howSum(8, [2, 3, 5]))    # [2, 2, 2, 2]
    print(howSum(300, [7, 14]))    # None