from abc import ABC, abstractmethod


class Fruit(ABC):

    @abstractmethod
    def ripen(self):
        pass

    def clean(self):
        pass

    @abstractmethod
    def sound(self):
        pass


class Watermelon(Fruit):

    def ripen(self):
        print("Ripening Watermelon")

    def sound(self):
        print("Squish Squish")


class Pear(Fruit):

    def ripen(self):
        print("Ripening Pear")

    def sound(self):
        print("Slice Slice")


class Peach(Fruit):

    def ripen(self):
        print("Ripening Peach")

    def sound(self):
        print("Chomp Chomp")


class Apple(Fruit):

    def ripen(self):
        print("Ripening Apple")

    def sound(self):
        print("Crunch Crunch")
