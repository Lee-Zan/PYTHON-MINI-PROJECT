class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_stock(self, amount):
        self.quantity += amount
        print("Stock updated: " + self.name + " now has " + str(self.quantity) + " units.")


    def update_price(self, new_price):
        self.price = new_price
        print("Price updated: " + self.name + " now costs " + str(self.price) + " per unit.")

    def show_info(self):
        print("Product: " + self.name + ", Quantity: " + str(self.quantity) + ", Price: " + str(self.price))


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.name in self.products:
            print(product.name + " already exists in inventory.")
        else:
            self.products[product.name] = product
            print(product.name + " added to inventory.")

    def check_availability(self, product_name):
        if product_name in self.products:
            product = self.products[product_name]
            print(product.name + " is available with " + str(product.quantity) + " units.")
        else:
            print(product_name + " is not found in inventory.")

    def show_all_products(self):
        if not self.products:
            print("Inventory is empty.")
        else:
            print("Inventory List:")
            for product in self.products.values():
                product.show_info()


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

inventory.show_all_products()

p1.update_stock(20)
p5.update_price(5)

inventory.check_availability("Rice")
inventory.check_availability("Orange")