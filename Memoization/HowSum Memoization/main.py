
def howSum(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    for num in numbers:
        remainder = targetSum - num
        valueReturned = howSum(remainder, numbers)
        # print(f'value returned = {valueReturned}')
        if valueReturned is not None:
            valueReturned.append(num)
            return valueReturned

    return None

if __name__ == "__main__":
    print(howSum(7, [2, 3]))
    print(howSum(7, [5, 3, 4, 7]))
    print(howSum(7, [2, 4]))
    print(howSum(8, [2, 3, 5]))
    print(howSum(300, [7, 14]))
    