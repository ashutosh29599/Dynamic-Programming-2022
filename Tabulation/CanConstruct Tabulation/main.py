
def canConstruct(target, wordBank):
    tab = [False] * (len(target) + 1)
    tab[0] = True

    for i in range(len(target)):
        if tab[i] == True:
            for word in wordBank:
                if target[i:(i + len(word))] == word:
                    tab[i + len(word)] = True

    return tab[len(target)]

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