from fruits import Fruit
from factories import FruitFactory


def throw_fruit(name: str) -> Fruit:
    fruit = FruitFactory.create_fruit(name)
    fruit.ripen()
    fruit.clean()
    return fruit
