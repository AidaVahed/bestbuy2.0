class Product:
    """Represents a product in the store."""

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        if not name or price < 0 or quantity < 0:
            raise Exception("Invalid product details")

    def get_quantity(self):
        """Returns the quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity):
        """Sets the quantity and deactivates the product if it reaches 0."""
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """Returns whether the product is active."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self):
        """Returns a string representation of the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """Buys a given quantity of the product."""
        if quantity > self.quantity:
            raise Exception("Not enough stock")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return self.price * quantity


class NonStockedProduct(Product):
    """Represents a product that has no stock."""

    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def show(self):
        """Returns a string representation of the non-stocked product."""
        return f"{self.name}, Price: {self.price}, Non-stocked product"


class LimitedProduct(Product):
    """Represents a product with a purchase limit."""

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        """Buys a given quantity with a purchase limit."""
        if quantity > self.maximum:
            raise Exception(f"Cannot buy more than {self.maximum} of {self.name}")
        return super().buy(quantity)

    def show(self):
        """Returns a string representation of the limited product."""
        return f"{self.name}, Price: {self.price}, Max Purchase Limit: {self.maximum}"
