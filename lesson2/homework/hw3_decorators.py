"""Домашнее задание. Тема 3: декораторы. Сделал 02.11"""


def hw_08(func):
    called = False
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal called
        if called:
            raise RuntimeError("Функция уже была вызвана")
        called = True
        return func(*args, **kwargs)
    return wrapper


def hw_09(*types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for value, expected_type in zip(args, types):
                if not isinstance(value, expected_type):
                    raise TypeError("Неверный тип аргумента")
            return func(*args, **kwargs)
        return wrapper
    return decorator


def hw_10(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.log.append(args)
        return func(*args, **kwargs)
    wrapper.log = []
    return wrapper