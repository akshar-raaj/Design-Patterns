from fruits import Fruit, Watermelon, Peach, Pear


def throw_fruit(name: str) -> Fruit:
    if name == "Watermelon":
        fruit = Watermelon()
    elif name == "Peach":
        fruit = Peach()
    elif name == "Pear":
        fruit = Pear()
    fruit.ripen()
    fruit.clean()
    return fruit
