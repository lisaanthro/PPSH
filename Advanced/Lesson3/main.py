from functools import reduce


def task1():
    print("'Женя, Вася'")


def task2():
    def solve(l) -> list:
        squares = list(map(lambda x: x ** 3, l))
        return squares

    l = map(int, input().split())
    print(solve(l))


def task3():  # [-1, -7, -8, -10]
    l = map(int, input().split())
    negative = list(filter(lambda x: x < 0, l))
    print(negative)


def task4():  # 40320
    n = int(input())
    fact = reduce(lambda x, y: x * y, range(1, n + 1))
    print(fact)


def task5():  # 6
    l = map(int, input().split())
    ans = reduce(lambda x, y: x if x > y else y, [x for x in l if (x ** 2) % 9 == 0])
    print(ans)


def main():
    # task1()
    # task2()
    # task3()
    # task4()
    task5()  # input: 2 4 6 8 0 3 4 2 3 5 1 2


if __name__ == '__main__':
    main()
