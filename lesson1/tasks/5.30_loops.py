def task_30(numbers, stop_value):
    total = 0
    for num in numbers:
        if num == stop_value:
            break
        total += num
    return total