def task1():
    print('4 1 \n 5 6')


def task2():
    print('ППШ')


def task3():
    print('bee')


def task4():  # True False
    a = [int(s) for s in range(1, 20)]
    print(a)
    iterator = iter(a)

    print(9 in iterator)  # iterator проходит по всем элементам, пока не найдет == 9. True
    print(next(iterator))  # points at 10
    print(11 in iterator)  # True
    print(next(iterator))  # points at 12
    print(11 in iterator)  # False
    try:
        print(next(iterator))  # StopIteration
    except StopIteration:
        print('iterator прошелся по всему листу, не нашел 9 и показывает на конец')


def task5():
    print('1 4 16')


def task6():  # 1 9 25
    squares = (x ** 2 for x in range(1, 6))
    # print(list(squares))
    it = iter(squares)
    print(next(it))  # 0
    next(it)
    print(next(it))  # 2
    next(it)
    print(next(it))  # 4


def task7():
    card_values = ['6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
    card_suits = ['Буби', 'Крести', 'Пики', 'Черви']

    card_deque = ((y + ' ' + x) for x in card_suits for y in card_values)
    iterator = iter(card_deque)
    print(next(iterator))  # 6 Буби
    print(next(iterator))  # 7 Буби
    for _ in range(10):
        next(iterator)
    print(next(iterator))  # 9 Крести


# Я решила поиграться и написать свой класс итератора по колоде карт, пока не доделала, позже вернусь и допишу
def task8():
    card_values = ['6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
    card_suits = ['Буби', 'Крести', 'Пики', 'Черви']

    class CardIterator:
        def __init__(self):
            self.value_id = -1
            self.suit_id = -1

        def __iter__(self):
            return self

        def __next__(self):
            if self.suit_id == (len(card_suits) - 1):
                raise StopIteration
            if self.value_id == (len(card_values) - 1):
                self.suit_id = self.suit_id + 1
            self.suit_id = (self.value_id + 1) % len(card_values)
            return f'{card_values[self.value_id]} {card_suits[self.suit_id]}'

    iterator = CardIterator
    print(next(iterator))


def main():
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    # task6()
    # task7()
    task8()


if __name__ == '__main__':
    main()
