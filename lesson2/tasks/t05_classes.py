"""Тема 5. Классы."""

from math import hypot

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"Гав! Я {self.name}, порода {self.breed}"


class Robot:
    count = 0

    def __init__(self):
        Robot.count += 1
        self.serial = Robot.count


class Settings:
    def __init__(self, **options):
        for key, value in options.items():
            setattr(self, key, value)

    def get(self, key, default=None):
        return getattr(self, key, default)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return hypot(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        if not isinstance(other, Money):
            return False

        return self.amount == other.amount and self.currency == other.currency


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def magnitude(self):
        return hypot(self.x, self.y)