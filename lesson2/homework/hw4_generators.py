"""Домашнее задание. Тема 4: генераторы. Сделал 03.11"""

from math import isqrt

def hw_11(n):
    for number in range(2, n + 1):
        for divisor in range(2, isqrt(number) + 1):
            if number % divisor == 0:
                break
        else:
            yield number


def hw_12(items, times):
    for _ in range(times):
        yield from items


def hw_13(items, size):
    if size <= 0:
        raise ValueError("Размер части должен быть положительным")

    chunk = []

    for item in items:
        chunk.append(item)

        if len(chunk) == size:
            yield chunk
            chunk = []

    if chunk:
        yield chunk


def hw_14(items):
    iterator = iter(items)

    try:
        previous = next(iterator)
    except StopIteration:
        return

    for current in iterator:
        yield previous, current
        previous = current