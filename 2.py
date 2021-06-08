from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, parro):
        self.parr = parro

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    @property
    def fabric_consumption(self):
        return self.parr / 6.5 + 0.5


class Suit(Clothes):
    @property
    def fabric_consumption(self):
        return self.parr * 2 + 0.3


a = Suit(24)
b = Coat(34)
print(a.fabric_consumption)
print(b.fabric_consumption)
