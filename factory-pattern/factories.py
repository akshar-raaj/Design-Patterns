from abc import ABC, abstractmethod

from fruits import Fruit, Watermelon, Peach, Pear, Apple


class FruitFactory(ABC):

    def throw_fruit(self):
        fruit = self.create_fruit()
        fruit.ripen()
        fruit.clean()
        return fruit

    @abstractmethod
    def create_fruit(self) -> Fruit:
        pass


class WatermelonFactory(FruitFactory):

    def create_fruit(self):
        return Watermelon()


class PeachFactory(FruitFactory):

    def create_fruit(self):
        return Peach()


class PearFactory(FruitFactory):

    def create_fruit(self):
        return Pear()


class AppleFactory(FruitFactory):

    def create_fruit(self):
        return Apple()
