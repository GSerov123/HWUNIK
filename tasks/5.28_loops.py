def task_28(names, days):
    result = {}
    for name, d in zip(names, days):
        result[name] = d
    return result