from abc import ABCMeta, abstractmethod


class Observer(object, metaclass=ABCMeta):

    @abstractmethod
    def update(self, customer_id):
        pass


class ConfigureCustomer(Observer):
    """
    Create associated entities needed for proper functioning of a customer.
    """

    def __init__(self, customer_service):
        self.customer_service = customer_service
        self.customer_service.add_observer(self)

    def update(self, customer_id):
        self.configure_customer(customer_id)

    def configure_customer(self, customer_id):
        # Logic to insert rows in other tables for the customer
        print(f"Configuring customer {customer_id}")


class SendWelcomeEmail(Observer):

    def __init__(self, customer_service):
        self.customer_service = customer_service
        self.customer_service.add_observer(self)

    def update(self, customer_id):
        self.send_welcome_email(customer_id)

    def send_welcome_email(self, customer_id):
        # Logic to send welcome email
        print(f"Sending welcome email to customer {customer_id}")


class NotifyOperations(Observer):

    def __init__(self, customer_service):
        self.customer_service = customer_service
        self.customer_service.add_observer(self)

    def update(self, customer_id):
        self.notify_operations(customer_id)

    def notify_operations(self, customer_id):
        # Logic to notify operations
        print(f"Notifying operations for customer {customer_id}")


class NotifySupport(Observer):

    def __init__(self, customer_service):
        self.customer_service = customer_service
        self.customer_service.add_observer(self)

    def update(self, customer_id):
        self.notify_support(customer_id)

    def notify_support(self, customer_id):
        # Logic to notify support
        print(f"Notifying support for customer {customer_id}")