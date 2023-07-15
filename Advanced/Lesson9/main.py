def task1():
    a, b = map(float, input()[1:-1].split(' / '))  # if input starts and ends with "
    try:
        return a / b
    except ZeroDivisionError:
        return 'ERROR'


def task2(*args) -> list:  # better call it passwords, not args
    possible_passwords = []
    for password in args:
        try:
            converted = int(password, 16)
            possible_passwords.append(password)
        except ValueError:
            pass
    return possible_passwords


def task3():
    olympiad1 = {"name": "Пробная вышка",
                 "winners": {
                     "Олеся Олимпиадникова": 594,
                     "Олег Олимпиадников": 587,
                     "Онисим Олимпиадников": 581
                 }
                 }
    olympiad2 = {"name": "Горные воробьи",
                 "winners": {
                     "Ольга Олимпиадникова": (20, 20, 19, 20),
                     "Олеся Олимпиадникова": (19, 19, 20, 20, 17),
                     "Офелия Олимпиадников": (20, 20, 20, 20, 13)
                 }
                 }

    def winner_check(name):
        print(f'\n{name}:')
        try:
            print(f'{olympiad1["name"]} победитель {olympiad1["winners"][name]}')
        except KeyError:
            print(f'{olympiad1["name"]} призер')
        finally:
            print('-' * 20)

        try:
            is_winner = olympiad2["winners"][name]
            print(f'{olympiad2["name"]} победитель {is_winner[4]}')
        except KeyError:
            print(f'{olympiad2["name"]} призер')
        except IndexError:
            print(f'{olympiad2["name"]} победитель')
        finally:
            print('-' * 20)

    for first_name in ['Ольга', 'Олеся']:
        winner_check(first_name + ' Олимпиадникова')


def task4():
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print('interrupted')
        while True:
            pass


def task5():
    class LizardInLemonadeMug(Exception):
        pass

    class BarIsBurned(Exception):
        pass

    def order(bar_mugs=100):
        try:
            placed_order = input('Сделайте заказ на кружки лимонада, пожалуйста!')
            if placed_order == 'ящерица в стакане':
                raise LizardInLemonadeMug
            if placed_order == 'где туалет?':
                raise BarIsBurned
            mug_count = int(placed_order)
            assert mug_count < bar_mugs, f'Извините, лимонада осталось лишь {bar_mugs} стаканов.'
            if 0 < mug_count < 1000:
                raise ValueError
        except LizardInLemonadeMug:
            print('Ящериц нет.')
        except BarIsBurned:
            print('Вы сгорели(')
            return
        except AssertionError:
            print(f'Бар маленький, у нас всего {bar_mugs} кружек.')
        except ValueError:
            print('Введите реальное число кружек.')
        finally:
            print('Ждем вас снова!')
            order()

    order()


def main():
    # print(task1())
    # print(task2('sfhs10', '12d'))
    # task3()
    # task4()
    task5()


if __name__ == '__main__':
    main()
