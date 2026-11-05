"""Тема 4. Генераторы и yield."""


def task_19(n):
    for number in range(1, n + 1):
        yield number * 2


def task_20(n):
    for number in range(n, -1, -1):
        yield number


def task_21(n):
    return (number ** 2 for number in range(1, n + 1))


def task_22():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


def task_23(items):
    seen = []

    for item in items:
        if item not in seen:
            seen.append(item)
            yield item

def task_24(nested):
    for sublist in nested:
        yield from sublist