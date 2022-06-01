import copy

def bestSum(targetSum, numbers):
    tab = [None] * (targetSum + 1)
    tab[0] = []

    for i in range(targetSum):
        if tab[i] != None:
            for num in numbers:
                temp = copy.deepcopy(tab[i])
                combo = copy.deepcopy(temp)
                combo.append(num)

                if (i + num) <= targetSum:
                    if ((tab[i + num] == None) or (len(combo) < len(tab[i + num]))):
                        tab[i + num] = combo

    return tab[targetSum]


if __name__ == "__main__":
    print(bestSum(7, [5, 3, 4, 7]))    # [7]
    print(bestSum(8, [2, 3, 5]))    # [3, 5]
    print(bestSum(8, [1, 4, 5]))    # [4, 4]
    print(bestSum(100, [1, 2, 5, 25]))    # [25, 25, 25, 25]
