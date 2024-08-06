from fruits import Fruit
from factories import WatermelonFactory, PeachFactory


def throw_fruit() -> Fruit:
    watermelon_factory = WatermelonFactory()
    watermelon_factory.throw_fruit()

    peach_factory = PeachFactory()
    peach_factory.throw_fruit()
