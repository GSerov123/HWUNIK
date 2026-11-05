"""Домашнее задание. Тема 1: функции и аргументы. Сделал 01.11"""


def hw_01(*args):
    if not args:
        return 0
    return sum(args) / len(args)


def hw_02(n):
    if n <= 1:
        return n
    return hw_02(n - 1) + hw_02(n - 2)


def hw_03(tag, *items, sep=", "):
    text = sep.join(str(item) for item in items)
    return f"{tag}: {text}"

def hw_04(prefix, **kwargs):
    return {
        key: value
        for key, value in kwargs.items()
        if key.startswith(prefix)
    }