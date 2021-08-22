# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def prntarea(self):
        return 0


class Square(Shape):
    sides = 4

    def __init__(self):
        self.side = 10

    def prntarea(self):
        return self.side*self.side


s1 = Square()
print(s1.prntarea())
