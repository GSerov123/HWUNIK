import math

def hw_01(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def hw_02(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def hw_03(card):
    return "*" * max(len(card) - 4, 0) + card[-4:]

def hw_04(x, y):
    return f"{x} / {y} = {x / y:.2f}"

def hw_05():
    total = 0

    def acc(x):
        nonlocal total
        total += x
        return total

    return acc

def hw_06(settings, defaults):
    return {**defaults, **settings}

def hw_07(month):
    if month in (12, 1, 2):
        return "зима"
    if 3 <= month <= 5:
        return "весна"
    if 6 <= month <= 8:
        return "лето"
    if 9 <= month <= 11:
        return "осень"
    return None

def hw_08(p1, p2):
    beats = {"камень": "ножницы", "ножницы": "бумага", "бумага": "камень"}
    if p1 == p2:
        return "ничья"
    return "игрок 1" if beats[p1] == p2 else "игрок 2"

def hw_09(a, b, c):
    return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a

def hw_10(n):
    if 11 <= n % 100 <= 14:
        return "лет"
    last = n % 10
    if last == 1:
        return "год"
    if 2 <= last <= 4:
        return "года"
    return "лет"

from collections import Counter

def hw_11(text):
    return Counter(text.split()).most_common(1)[0][0]

def hw_12(matrix):
    return [sum(row) for row in matrix]

def hw_13(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def hw_14(mapping):
    return {v: k for k, v in mapping.items()}

def hw_15(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def hw_16(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def hw_17(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("fizzbuzz")
        elif i % 3 == 0:
            result.append("fizz")
        elif i % 5 == 0:
            result.append("buzz")
        else:
            result.append(str(i))
    return result

def hw_18(s):
    parts = s.split()
    if len(parts) != 2:
        return None
    try:
        return int(parts[0]), int(parts[1])
    except ValueError:
        return None

def hw_19(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

def hw_20(age):
    if not isinstance(age, int) or isinstance(age, bool):
        raise TypeError("Возраст должен быть целым числом")
    if not 0 <= age <= 120:
        raise ValueError("Возраст должен быть от 0 до 120")
    return age