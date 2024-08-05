from abc import ABC, abstractmethod


class Fruit(ABC):

    @abstractmethod
    def ripen(self):
        pass

    def clean(self):
        pass


class Watermelon(Fruit):

    def ripen(self):
        print("Ripening Watermelon")


class Pear(Fruit):

    def ripen(self):
        print("Ripening Pear")


class Peach(Fruit):

    def ripen(self):
        print("Ripening Peach")