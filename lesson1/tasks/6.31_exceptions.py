def task_31(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None