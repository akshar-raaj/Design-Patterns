from fruits import Fruit, Watermelon, Peach, Pear

class FruitFactory(object):

    @staticmethod
    def create_fruit(name) -> Fruit:
        if name == "Watermelon":
            return Watermelon()
        elif name == "Peach":
            return Peach()
        elif name == "Pear":
            return Pear()
