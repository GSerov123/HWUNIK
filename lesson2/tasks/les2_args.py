"""Тема 2. args"""

def task_07(*args):
    result = 1
    for number in args:
        result *= number
    return result


def task_08(**kwargs):
    return "; ".join(f"{key}={kwargs[key]}" for key in sorted(kwargs))


def task_09(func, args, kwargs):
    return func(*args, **kwargs)


def task_10(words):
    return sorted(words, key=lambda word: (len(word), word))


def task_11(numbers):
    even_numbers = filter(lambda number: number % 2 == 0, numbers)
    return list(map(lambda number: number ** 2, even_numbers))


def task_12(f, g):
    return lambda x: f(g(x))