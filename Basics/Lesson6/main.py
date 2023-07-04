def task1():
    l = []
    n = int(input())
    m = int(input())
    l.append(n)
    l.append(m)
    print(l)
    print(sum(l))  # 46


def task2():
    words = input().split()
    l = []
    for word in words:
        l.append(word)
    print(l[0], l[-1])  # Программирование школы


def task3():
    words = input().split()
    l = []
    for word in words:
        l.append(word)
    max_len = 0
    max_word = ''
    for word in l:
        if len(word) > max_len:
            max_len = len(word)
            max_word = word
    print(max_word)  # нетипичный


def task4():
    n = int(input())
    l = []
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            l.append(i)
    print(sum(l))   # 234168


def task5():
    words = input().split()
    l = []
    for word in words:
        l.append(word)
    max_count = 0
    max_word = ''
    for word in l:
        cur_count = l.count(word)
        if max_count < cur_count:
            max_count = cur_count
            max_word = word
    print(max_word)     # cat


def main():
    task1()
    task2()
    task3()
    task4()
    task5()


if __name__ == '__main__':
    main()
