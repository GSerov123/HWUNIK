def task_02(total_seconds):
    hours = total_seconds // 3600
    remaining_after_hours = total_seconds % 3600

    minutes = remaining_after_hours // 60
    seconds = remaining_after_hours % 60

    return hours, minutes, seconds

print(task_02(3661))
print(task_02(59))
print(task_02(0))