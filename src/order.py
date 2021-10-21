
class Order:
    def __init__(self, customer_name, customer_address, customer_phone, courier, status, items):
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.customer_phone = customer_phone
        self.courier = courier
        self.status = status
        self.items = items
        pass