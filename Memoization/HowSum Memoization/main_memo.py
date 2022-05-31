
def howSum(targetSum, numbers, memo = {}):
    if targetSum in memo.keys():
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    for num in numbers:
        remainder = targetSum - num
        valueReturned = howSum(remainder, numbers, memo)
        # print(f'value returned = {valueReturned}')
        if valueReturned is not None:
            valueReturned.append(num)
            memo[targetSum] = valueReturned
            return valueReturned

    memo[targetSum] = None
    return None

if __name__ == "__main__":
    print(howSum(7, [2, 3], memo={}))   # [3, 2, 2]
    print(howSum(7, [5, 3, 4, 7], memo={})) # [4, 3]
    print(howSum(7, [2, 4], memo={}))   # None
    print(howSum(8, [2, 3, 5], memo={}))    # [2, 2, 2, 2]
    print(howSum(300, [7, 14], memo={}))    # None
    