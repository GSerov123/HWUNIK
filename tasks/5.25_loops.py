def task_25(n):
    total = 0
    while n > 0:
        total += n % 10  # добавляем последнюю цифру
        n //= 10  # убираем последнюю цифру
    return total