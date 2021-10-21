
class Product():
    def __init__(self, id, name, price, qty):
        self.id = id
        self.name = name
        self.price = price
        self.qty = qty

    def __str__(self):
        return f"id = {self.id}, name = {self.name}, price = {self.price}, quantity = {self.qty}"

    def __repr__(self):
        return f"Product(id = {self.id}, name = {self.name}, price = {self.price}, quantity = {self.qty})"
