"""Домашнее задание. Тема 2: функции высшего порядка и лямбды. Сделал 01.11"""


def hw_05(func, items):
    result = []
    for item in items:
        result.append(func(item))
    return result


def hw_06(predicate, items):
    result = []
    for item in items:
        if predicate(item):
            result.append(item)
    return result


def hw_07(words):
    return sorted(words, key=lambda word: (word[-1], word))