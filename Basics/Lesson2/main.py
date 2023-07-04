import string


def task1() -> bool:
    return True


def task2() -> bool:
    password1 = input()
    password2 = input()
    return password1 == password2  # False


def task3() -> int:
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    return min(a, b, c, d)


def task4() -> int:
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    return max(a, b, c, d)


def task5() -> bool:
    a = int(input())
    b = int(input())
    c = int(input())
    return (a < (b + c)) and (b < (a + c)) and (c < (a + b))


def task6() -> string:
    a = int(input())
    b = int(input())
    c = int(input())
    if not((a < (b + c)) and (b < (a + c)) and (c < (a + b))):
        return 'вырожденный'
    if a == b and a == c and b == c:
        return 'равносторонний'
    if (a == b and a != c) or (b == c and a != b) or (c == a and a != b):
        return 'равнобедренный'
    return 'разносторонний'


def task7() -> int:
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    if c < a:   # инвариант: первый отрезок всегда левее
        a, c = c, a
        b, d = d, b
    length = min(b, d) - max(a, c) + 1
    return length


def main():
    print(task1())
    print(task2())
    print(task3())
    print(task4())
    print(task5())
    print(task6())
    print(task7())


if __name__ == '__main__':
    main()
