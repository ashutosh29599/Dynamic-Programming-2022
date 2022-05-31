import copy
from distutils.dep_util import newer

def bestSum(targetSum, numbers, memo={}):
    if targetSum in memo.keys():
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    best = None

    for num in numbers:
        remainder = targetSum - num
        returnedValue = bestSum(remainder, numbers, memo)
        if returnedValue is not None:
            newReturn = copy.deepcopy(returnedValue)
            newReturn.append(num)

            if (best == None) or (len(newReturn) < len(best)):
                best = copy.deepcopy(newReturn)
        
    memo[targetSum] = best
    return best
    


if __name__ == "__main__":
    print(bestSum(7, [5, 3, 4, 7], memo={})) # [7]

    print(bestSum(8, [2, 3, 5], memo={}))    # [3, 5]

    print(bestSum(8, [1, 4, 5], memo={}))    # [4, 4]

    print(bestSum(100, [1, 2, 5, 25], memo={})) #[25, 25, 25, 25]

    