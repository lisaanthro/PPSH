def my_sum(arr) -> int:
    ssum = 0
    for x in arr:
        ssum += x
    return ssum


def task1():
    arr = [1, 7, 42, 12, 10, 1, 4, 0]
    print(my_sum(arr))  # 77


def check_range(n) -> bool:
    return 1 <= n <= 9


def task2():
    n = int(input())
    print(check_range(n))   # True


def perfect(n) -> bool:
    div_sum = 0
    for i in range(1, n):
        if n % i == 0:
            div_sum += i
    return div_sum == n


def task3():
    n = int(input())
    print(perfect(n))   # True


def check_poly(s):
    return s == s[::-1]


def task4():
    s = input()
    print(check_poly(s))    # False


def simple(n) -> bool:
    for i in range(2, n):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return True


def task5():
    n = int(input())
    print(simple(n))    # False


def recursive_fibonacci(n) -> int:
    if n == 1:
        return 0
    if n == 2 or n == 3:
        return 1
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def task6():
    n = int(input())
    print(recursive_fibonacci(n))   # 34


def main():
    # task1()
    # task2()
    # task3()
    task4()
    # task5()
    # task6()


if __name__ == '__main__':
    main()