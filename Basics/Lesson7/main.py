def task1():
    print(sum([x ** 2 for x in range(1, 100)]))     # 328350


def task2():
    print('[0, 8, 16, 24, 32]')


def task3():
    even = [x for x in range(1, 21) if x % 2 == 0]
    print(len(even))   # 10


def task4():
    arr = [64, 8, 72, 1, 56, 78, 7, 59, 9, 80]
    even = [x for x in arr[::2] if x % 2 == 0]
    print(len(even))    # 3


def task5():
    numbers = [x for x in range(1, 1000) if x % 7 == 0 or x % 11 == 0]
    print(len(numbers))     # 220


def main():
    # task1()
    # task2()
    # task3()
    # task4()
    task5()


if __name__ == '__main__':
    main()