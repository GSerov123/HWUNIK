"""Домашнее задание. Тема 6: инструменты класса. Сделал 05.11"""


class Employee:
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role

    @classmethod
    def from_string(cls, text):
        name, age, role = text.split(";")
        return cls(name, int(age), role)


class Password:
    def __init__(self, raw):
        self._password = raw

    @property
    def password(self):
        return "*" * len(self._password)

    @property
    def is_strong(self):
        return (
            len(self._password) >= 8
            and any(char.isupper() for char in self._password)
            and any(char.isdigit() for char in self._password)
        )

    def check(self, candidate):
        return candidate == self._password


class Stats:
    def __init__(self, values):
        self._values = list(values)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, index):
        return self._values[index]

    def mean(self):
        if not self._values:
            return None

        return sum(self._values) / len(self._values)