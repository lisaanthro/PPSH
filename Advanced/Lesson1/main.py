import copy
import sys


def task1():
    R = [45, 84, 10, 58]
    A = R
    R[0] = 54
    print(A[0] + R[0], 'is 108')


def task2():
    l0 = list(map(int, input().split()))
    l1 = l0[:]
    l2 = l0.copy()
    l3 = copy.copy(l0)
    l4 = copy.deepcopy(l0)
    l5 = list(l0)
    print(sys.getrefcount(l0)) # 2 refcount
    print(5, sum(l0))


def task3():
    AR = [[90, 99, 109, 119]] * 4
    AR[0][0], AR[3][3] = 890, 76
    print(AR[1][0] + AR[2][3], 'is 966 ')


def task4():
    animals = ['cat', 'cat', 'dog', 'dog', 'bird', 'capybara', 'capybara', 'capybara']
    animals_count = {}
    for animal in animals:
        if animal in animals_count:
            animals_count[animal] += 1
        else:
            animals_count[animal] = 1

    for key in animals_count:
        print(sys.getrefcount(key))
    for i in range(1, 4):
        print(sys.getrefcount(i))


def task5():
    backpack = ["capybara", "capyraba", "capyba", "capyba", "capybara", 2999, 2999, "capybara", [7, 7, 7],
                [7, 7, 7], [7, 7, 7], [7, 7, 7]] + [[8, 8]] * 5
    print(backpack)
    same_object, equal_value = 0, 0
    for i in range(0, len(backpack)):
        for j in range(i + 1, len(backpack)):
            if backpack[i] is backpack[j]:
                same_object += 1
            if backpack[i] == backpack[j]:
                equal_value += 1
    print(same_object, equal_value)  # если выводить значения, можно заменить, что [7,7,7] ссылаются на разные объекты


def task6():
    recursive_salad = ['lettuce', 'chicken', 'cheese', 'sause', 'tomatoes', 'croutons']
    recursive_salad.append(recursive_salad)
    recursive_salad = copy.copy(recursive_salad)
    recursive_salad[6] += ['salt', 'pepper']
    # print(recursive_salad[6][6])
    # print(recursive_salad)
    print(recursive_salad[6][6][4], recursive_salad[6][-1])  # tomatoes, pepper


def main():
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    task6()


if __name__ == '__main__':
    main()
