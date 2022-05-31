 
def canConstruct(target, wordBank):
    if target == "":
        return True
    
    # We will only deal with word that are suffixes; words in middle will change the target
    for word in wordBank:
        if word in target:
            if target.index(word) == 0: # the word is a suffix
                # print(f"target, word = {target}, {word}")
                newTarget = target.split(word, 1)[1]    # Python 3.9 has str.removesuffix("suffix")
                if canConstruct(newTarget, wordBank) == True:
                    return True

    return False

if __name__ == "__main__":
    print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))   # true
    print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))    # false
    print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))    # true
    print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",\
            ["e",\
             "ee",\
             "eee",\
             "eeee",\
             "eeeee",\
             "eeeeee"]))    # false