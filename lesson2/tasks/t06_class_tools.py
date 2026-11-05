"""Тема 6. Инструменты класса: classmethod, staticmethod, property, магические методы."""

import math

class MathUtils:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def celsius_to_fahrenheit(c):
        return c * 9 / 5 + 32

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, text):
        year, month, day = map(int, text.split("-"))
        return cls(year, month, day)


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self._balance = value

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Размер пополнения не может быть отрицательным")
        self.balance += amount


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


class Numbers:
    MULTIPLIER = 3.5

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    @classmethod
    def multiply(cls, a):
        return a * cls.MULTIPLIER

    @staticmethod
    def subtract(b, c):
        return b - c

    @property
    def value(self):
        return self.x, self.y

    @value.setter
    def value(self, pair):
        self.x, self.y = pair