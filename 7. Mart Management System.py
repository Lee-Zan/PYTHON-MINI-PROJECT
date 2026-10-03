class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.name in self.products:
            print(product.name + " already exists in inventory.")
        else:
            self.products[product.name] = product
            print(product.name + " added to inventory.")

p1 = Product("Dairy Milk", 50, 25)
p2 = Product("Rice", 2500, 15)
p3 = Product("Banana", 100, 5)
p4 = Product("Biscuits", 10, 50)
p5 = Product("Noodles", 25, 7)

inventory = Inventory()
inventory.add_product(p1)
inventory.add_product(p2)
inventory.add_product(p3)
inventory.add_product(p4)
inventory.add_product(p5)

