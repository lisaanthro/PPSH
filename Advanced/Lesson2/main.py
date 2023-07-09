def task1():
    print('4 1 \n 5 6')


def task2():
    print('ППШ')


def task3():
    print('bee')


def task4():    # True False
    a = [int(s) for s in range(1, 20)]
    print(a)
    iterator = iter(a)

    print(9 in iterator) # iterator проходит по всем элементам, пока не найдет == 9. True
    print(next(iterator)) # points at 10
    print(11 in iterator) # True
    print(next(iterator)) # points at 12
    print(11 in iterator) # False
    try:
        print(next(iterator)) # StopIteration
    except StopIteration:
        print('iterator прошелся по всему листу, не нашел 9 и показывает на конец')


def task5():
    print('1 4 16')


def task6():    # 1 9 25
    squares = (x ** 2 for x in range(1, 6))
    # print(list(squares))
    it = iter(squares)
    print(next(it)) # 0
    next(it)
    print(next(it)) # 2
    next(it)
    print(next(it)) # 4


def task7():
    pass


def main():
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    task6()


if __name__ == '__main__':
    main()