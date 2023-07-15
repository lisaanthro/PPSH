def task1():
    def sum_numbers(*numbers) -> int:
        return sum(numbers)

    print(sum_numbers(1, 2, 3))  # 6
    print(sum_numbers(10, 20, 30, 40))  # 100


def task2():
    def print_kwargs(**kwargs):
        for key, value in kwargs.items():
            print(f'{key}: {value}')

    print_kwargs(name='Alice', age=25, country='USA')


def task3():
    def filter_by_length(min_length, *args):
        return [s for s in args if len(s) >= min_length]

    strings = ["hello", "world", "how", "are", "you"]
    print(filter_by_length(4, *strings))
    print(filter_by_length(3, *strings))


def task4():
    def calculate_total_price(price, **sales) -> float:
        total_sale = 0
        for sale_price in sales.values():
            total_sale += price * sale_price / 100
        return max(0, price - total_sale)

    print(calculate_total_price(100, student=10, coupon=20))  # 70.0
    print(calculate_total_price(200, holiday=25))  # 150.0
    print(calculate_total_price(500))  # 500


def task5():
    def custom_print(*args, **kwargs):
        custom_sep = ' '
        if 'sep' in kwargs:
            custom_sep = kwargs['sep']
        custom_end = ''
        if 'end' in kwargs:
            custom_end = kwargs['end']
        output = ''
        for arg in args:
            output += str(arg) + custom_sep
        for key, value in kwargs.items():
            if key == 'sep' or key == 'end':
                continue
            output += key + '=' + str(value) + custom_sep

        print(output.rstrip(custom_sep) + custom_end)

    custom_print(1, 2, 3, a=4, b=5, sep='-', end='!')
    custom_print('Hello', 'World', sep=' ')
    custom_print('apple', 'banana', 'cherry', sep=', ')
    custom_print(a=1, b=2, end='...')


def main():
    # task1()
    # task2()
    task3()
    # task4()
    # task5()


if __name__ == '__main__':
    main()
