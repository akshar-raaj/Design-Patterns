class Pizza(object):

    pass


class Margherita(Pizza):

    def get_price(self):
        return 1.0


class FarmHouse(Pizza):

    def get_price(self):
        return 1.5


class PeppyPaneer(Pizza):

    def get_price(self):
        return 1.75
