
def fib(n):
    fib_table = [0] * (n + 1)
    fib_table[1] = 1

    for i in range(0, n - 1):
        fib_table[i + 2] += fib_table[i] + fib_table[i + 1]

    # for item in fib_table:
    #     print(item, end=', ')
    return fib_table[n]


if __name__ == "__main__":
    print(fib(6))  # 8
    print(fib(7))  # 13
    print(fib(8))  # 21
    print(fib(50)) # 12586269025