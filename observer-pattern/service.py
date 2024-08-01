from observers import Observer

class CustomerService(object):

    def __init__(self, data):
        self.data = data
        self.observers: list[Observer] = []

    def add_observer(self, observer):
        if hasattr(observer, 'update'):
            self.observers.append(observer)
        else:
            # Log it as an exception
            pass

    def delete_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self, customer_id):
        for observer in self.observers:
            # Assume that the update method is implemented in the Observer class
            observer.update(customer_id)

    def create_customer(self):
        # Logic to insert a row in the database
        dummy_customer_id = 100
        self.notify_observers(dummy_customer_id)