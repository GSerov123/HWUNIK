from abc import ABC, abstractmethod


class TextTransformer:
    """Задание 18. Цепочка правил (композиция функций).

    Конструктор принимает rules — список функций str → str. Метод
    apply(text) прогоняет текст через правила ПО ПОРЯДКУ и возвращает
    результат последнего преобразования.

    Примеры:
        t = TextTransformer([str.upper, lambda s: s.replace(" ", "_")])
        t.apply("hello world") == "HELLO_WORLD"
        TextTransformer([]).apply("как есть") == "как есть"
    """

    def __init__(self, rules):
        self.rules = rules

    def apply(self, text):
        for rule in self.rules:
            text = rule(text)
        return text


class PaymentMethod(ABC):
    """Задание 19. Методы оплаты: стратегии за общим интерфейсом.

    Абстрактный pay(amount) → строка. Реализации:
      CardMethod: "оплачено картой {amount}"
      CashMethod: "оплачено наличными {amount}"
    Checkout(method).pay(amount) делегирует вызов методу оплаты.

    Примеры:
        Checkout(CardMethod()).pay(100) == "оплачено картой 100"
        Checkout(CashMethod()).pay(250) == "оплачено наличными 250"
    """

    @abstractmethod
    def pay(self, amount):
        pass


class CardMethod(PaymentMethod):
    def pay(self, amount):
        return f"оплачено картой {amount}"


class CashMethod(PaymentMethod):
    def pay(self, amount):
        return f"оплачено наличными {amount}"


class Checkout:
    def __init__(self, method):
        self.method = method

    def pay(self, amount):
        return self.method.pay(amount)


class Sword:
    """Задание 20. Персонаж со сменным оружием.

    Sword.attack() → "удар мечом"; Bow.attack() → "выстрел из лука".
    Character(name, weapon): attack() возвращает "{name}: {атака оружия}";
    set_weapon(weapon) меняет оружие на ходу.

    Примеры:
        hero = Character("Ратибор", Sword())
        hero.attack() == "Ратибор: удар мечом"
        hero.set_weapon(Bow())
        hero.attack() == "Ратибор: выстрел из лука"
    """

    def attack(self):
        return "удар мечом"


class Bow:
    def attack(self):
        return "выстрел из лука"


class Character:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def set_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        return f"{self.name}: {self.weapon.attack()}"