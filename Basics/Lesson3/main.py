def task1():
    return '(x % 2 != 0) and (x % 10 != 5)'


def task2():
    return 'i, 10'


def task3() -> int:
    k = int(input())
    n = int(input())
    sum = 0
    cur = k + (k % 2 == 0)
    while cur <= n:
        sum += cur
        cur += 2
    return sum


def task4():
    n = int(input())
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


def main():
    print(task1())
    print(task2())
    print(task3())
    print(task4())


if __name__ == '__main__':
    main()
