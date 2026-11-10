import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Задание 31. Базовый абстрактный класс.

    Shape — абстрактный класс с абстрактным методом area().
    Реализуйте подклассы Circle(r) и Rectangle(w, h), вычисляющие площадь.
    Экземпляр Shape создать нельзя.

    Примеры:
        Shape()   # TypeError: абстрактный класс
        Circle(2).area() == 4 * math.pi
        Rectangle(3, 4).area() == 12
    """

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Animal(ABC):
    """Задание 32. Конкретный метод на абстрактной базе (шаблонный метод).

    Абстрактный метод speak(); конкретный метод introduce() возвращает
    "Я говорю: {speak()}" — он готов к работе, как только подкласс
    реализует speak(). Подкласс Cat: speak() → "мяу".

    Примеры:
        Cat("Мурка").introduce() == "Я говорю: мяу"
        Animal("X")   # TypeError: speak не реализован
    """

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass

    def introduce(self):
        return f"Я говорю: {self.speak()}"


class Cat(Animal):
    def speak(self):
        return "мяу"


class Vehicle(ABC):
    """Задание 33. Абстрактное свойство.

    Vehicle объявляет абстрактное СВОЙСТВО max_speed (через
    @property + @abstractmethod). Подкласс Car реализует его константой 220.

    Примеры:
        Vehicle()   # TypeError
        Car("Лада").max_speed == 220
    """

    @property
    @abstractmethod
    def max_speed(self):
        pass


class Car(Vehicle):
    def __init__(self, model):
        self.model = model

    @property
    def max_speed(self):
        return 220


class Plugin(ABC):
    """Задание 34. Реестр подклассов.

    Абстрактный run(). Классовый метод subclasses() возвращает отсортированный
    список имён ПРЯМЫХ подклассов того класса, у которого вызван
    (cls.__subclasses__()).

    Примеры:
        class Echo(Plugin):
            def run(self): return "echo"

        "Echo" in Plugin.subclasses()
        Echo().run() == "echo"
    """

    @abstractmethod
    def run(self):
        pass

    @classmethod
    def subclasses(cls):
        return sorted(subclass.__name__ for subclass in cls.__subclasses__())


class Serializable(ABC):
    """Задание 35, часть 1. Интерфейс сериализации."""

    @abstractmethod
    def to_dict(self):
        pass


def task_35(items):
    """Задание 35, часть 2. Работа через интерфейс, а не через тип.

    Верните список словарей для всех items, вызывая to_dict(). Функция
    принимает любые объекты, реализующие интерфейс Serializable, —
    без isinstance-проверок.

    Примеры:
        class Book(Serializable):
            def __init__(self, title):
                self.title = title
            def to_dict(self):
                return {"title": self.title}

        task_35([Book("а"), Book("б")]) == [{"title": "а"}, {"title": "б"}]
        task_35([]) == []
    """
    return [item.to_dict() for item in items]


class Item:
    """Задание 36, часть 1. Предмет: имя и стоимость (из упражнения 3 книги)."""

    def __init__(self, name, value):
        self.name = name
        self.value = value


class Box(ABC):
    """Задание 36, часть 2. Абстрактная коробка (по упражнению 3 книги).

    Абстрактные методы:
      add(item)  — положить предмет;
      empty()    — забрать ВСЕ предметы и вернуть их списком;
      count()    — сколько предметов сейчас в коробке.

    Реализуйте два подкласса с разным внутренним хранением:
      ListBox  — хранит предметы в списке;
      DictBox  — хранит в словаре.
    """

    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def empty(self):
        pass

    @abstractmethod
    def count(self):
        pass


class ListBox(Box):
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def empty(self):
        items = self._items
        self._items = []
        return items

    def count(self):
        return len(self._items)


class DictBox(Box):
    def __init__(self):
        self._items = {}
        self._next_key = 0

    def add(self, item):
        self._items[self._next_key] = item
        self._next_key += 1

    def empty(self):
        items = list(self._items.values())
        self._items = {}
        return items

    def count(self):
        return len(self._items)


def task_36(*boxes):
    """Задание 36, часть 3. Переупаковка коробок (по книге).

    Соберите все предметы из всех коробок и распределите их между коробками
    как можно равнее (первые коробки могут получить на один предмет больше).
    Порядок предметов не важен. Функция работает с ЛЮБЫМИ подклассами Box.

    Примеры:
        b1, b2, b3 = ListBox(), ListBox(), DictBox()
        # ... 20, 9 и 5 предметов ...
        task_36(b1, b2, b3)
        sorted(b.count() for b in (b1, b2, b3)) == [11, 11, 12]
    """
    all_items = []
    for box in boxes:
        all_items.extend(box.empty())
    for i, item in enumerate(all_items):
        boxes[i % len(boxes)].add(item)