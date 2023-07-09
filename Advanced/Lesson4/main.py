def task1():
    middle_name = 'Романович'
    for first_name in ['Александр', 'Алекс', 'Альберт']:
        for last_name in ['Вотяк', 'Вотяков', 'Вотякович']:
            print(f'Диплом с отличием вручается {last_name}у {first_name}у {middle_name}у.')


def task2():
    a, b, c = input(), input(), input()
    print(f'{a}{b:>04}-{c:>03}')


def task3():
    a = int(input())
    b = int(input())
    print(f'{a:>11}\n{b:>11}\n{a + b:>11}')


def task4():
    sum = 100000000.0
    r = int(input())
    months = int(input())
    for i in range(months):
        sum += sum * r / 100
    print(f'{sum:,.2f}')


def task5():
    for a in range(1, 101):
        for b in range(1, 101):
            result = a * b
            if '0' in str(result):
                print(f'"[DEBUG] {a=} {b=} {result=}"')


def task6(a, b, c, d):
    ip_template = ['{:08b}.', '{:b}.', '{:o}.', '{}.', '{:x}.']
    ips = []
    for template in ip_template:
        ips.append((template*4)[:-1].format(a, b, c, d))
    for ip in ips:
        print(ip)


def main():
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    task6(127, 0, 0, 1)


if __name__ == '__main__':
    main()