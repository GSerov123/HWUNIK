def task_35(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "индекс вне диапазона"