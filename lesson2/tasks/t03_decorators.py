"""Тема 3. Замыкания и декораторы."""

def task_13(start=0):
        count = start
        def counter():
            nonlocal count
            count += 1
            return count
        return counter


def task_14(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper


def task_15(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper


def task_16(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper


def task_17(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for value in args + tuple(kwargs.values()):
            if isinstance(value, (int, float)) and value < 0:
                raise ValueError("Аргументы должны быть неотрицательными")
        return func(*args, **kwargs)
    return wrapper


def task_18(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return [func(*args, **kwargs) for _ in range(times)]
        return wrapper
    return decorator