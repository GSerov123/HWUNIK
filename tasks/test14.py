def task_04(price, discount_percent):
    discounted_price = price * (1 - discount_percent / 100)
    return round(discounted_price, 2)
print(task_04(1000, 25))      # 750.0
print(task_04(199.99, 10))   # 179.99
print(task_04(500, 0))       # 500.0
