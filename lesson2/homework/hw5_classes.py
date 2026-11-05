"""Домашнее задание. Тема 5: классы. Сделал 04.11"""

from collections import deque

class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def is_empty(self):
        return not self._items


class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.popleft()

    def size(self):
        return len(self._items)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self._books = []

    def add(self, book):
        self._books.append(book)

    def titles(self):
        return [book.title for book in self._books]

    def by_author(self, author):
        return [book.title for book in self._books if book.author == author]