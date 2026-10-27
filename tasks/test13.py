def task_03(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius
print(task_03(212) == 100.0)