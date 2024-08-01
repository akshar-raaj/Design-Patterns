from menu import Pizza


class Topping(Pizza):

    def __init__(self, pizza):
        self.pizza = pizza


class Jalapenos(Topping):

    def get_price(self):
        return 0.2 + self.pizza.get_price()


class Onion(Topping):

    def get_price(self):
        return 0.25 + self.pizza.get_price()


class Olive(Topping):

    def get_price(self):
        return 0.3 + self.pizza.get_price()