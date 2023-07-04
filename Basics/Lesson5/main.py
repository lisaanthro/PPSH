def task1():
    n = int(input())
    for i in range(n + 1):
        if i % 3 == 0 and i % 6 != 0:
            print(i)


def task2():
    n = int(input())
    for i in range(10, n + 1):
        if i % 2 == 0:
            print(i)


def task3() -> int:
    n = int(input())
    sum = 0
    cnt = 0
    start_value = 1
    if n % 2 == 0:
        start_value += 1
    for i in range(start_value, n + 1, 2):
        sum += i
        cnt += 1
    if n % 2 == 0:
        return cnt
    return sum


def task4():
    n = int(input())
    if n % 3 == 0:
        m = int(input())
        cnt = 0
        for i in range(1, n + 1):
            if i % m == 0:
                cnt += 1
        print(cnt)
    else:
        for i in range(1, n + 1):
            print(n ** i)


def task5() -> int:
    a = int(input())
    b = int(input())
    n = int(input())
    cnt = 0
    for i in range(n):
        x = int(input())
        if a * a + b * b == x * x and x > 10 and (x % 3 == 0 or x % 4 == 0):
            cnt += 1
    return cnt


def main():
    task1()
    task2()
    print(task3())
    task4()
    print(task5())


if __name__ == '__main__':
    main()