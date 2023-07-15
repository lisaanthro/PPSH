import time


def timer(func):
    def measure(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'The function has been working for {end_time - start_time} sec, the result is {result}.')
    return measure


@timer
def f(x):
    sum = 1
    for i in range(1, x):
        sum += i
    return sum


#можно ли сделать несколько функций в одном декораторе?

def task1():
    # func = timer(f) - no decorator
    # func(1000000)
    f(100000)


def my_cache(func):
    dict = {}
    def inside_func(*args, **kwargs):
        if not args[0] in dict:
            dict[args[0]] = func(args[0])
        return dict[args[0]]
    return inside_func


# @timer
@my_cache
def fib(x):
    if x <= 1:
        return 1
    return fib(x - 1) + fib(x - 2)


def task2():
    print(fib(100))


def logging(func):
    def inside_func(*args, **kwargs):
        with open('log.txt', 'a+') as log:
            log.write(f'{time.time()} - {func.__name__} called.\n')
        func(*args, **kwargs)
    return inside_func


@logging
def write_me():
    pass


def task3():
    write_me()


def retry(func):
    def inside_func(*args, **kwargs):
        ans = None
        counter = 0
        while ans is None and counter < 10:
            ans = func(*args, **kwargs)
            print(f'{counter} Result is {ans}.\n')
            time.sleep(0.5)
            counter += 1
    return inside_func


@retry
@logging
def returns_none():
    pass


def task4():
    returns_none()

def main():
    # task1()
    # task2() -- to work on decorator compositions
    # task3()
    task4()


if __name__ == '__main__':
    main()