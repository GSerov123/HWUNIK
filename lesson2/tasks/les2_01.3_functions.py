def task_03(n):
    if n <= 0:
        return 0
    return n + task_03(n - 1)