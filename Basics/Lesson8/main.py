def task1():
    for i in range(1, 11):
        cur_line = ''
        for j in range(1, 11):
            cur_line += str(i * j) + '\t'
        print(cur_line)


def task2(l, r):
    cnt = 0
    for x in range(l, r + 1):
        for y in range(l, r + 1):
            for k in range(l, r + 1):
                if x * x + y * y == k * k:
                    cnt += 1
    print(cnt)


def divs_sum(x) -> int:
    sum = 0
    for i in range(1, x):
        if x % i == 0:
            sum += i
    return sum


def task3():
    n = int(input())
    for i in range(1, n):
        for j in range(i + 1, n):
            if divs_sum(i) == j and divs_sum(j) == i:
                print(i, j)


def task4():
    n = 4
    ans = ''
    for i in range(1000, 9999):
        s = str(i)
        cur_sum = 0
        for c in s:
            cur_sum += int(c)**n
        if cur_sum == i:
            ans += str(i) + ' '
    print(ans)


def main():
    task1()
    task2(10, 50)
    task3()
    task4()


if __name__ == '__main__':
    main()