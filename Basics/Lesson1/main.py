from math import sqrt


def task1():
    print(input() + input() + input())


def task2():
    a = int(input())
    b = int(input())
    print(2 ** 8 * a ** 8 - 2 ** 4 * a ** 4 + 2 ** 2 * a ** 2 - 2 * b + 1 / 2 * sqrt(b) + a * b ** (a + b) / 2)


def task3():
    a = input()
    b = input()
    print(a + b, end='!')  # 23!


def task4():
    print('(123 + 456 − 789) % 10 = 0')


def task5():
    x = int(input())
    print(x + 1, x - 1, sep='')


def task6():
    km = int(input())
    print(km // 100000)


def main():
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()


if __name__ == '__main__':
    main()
