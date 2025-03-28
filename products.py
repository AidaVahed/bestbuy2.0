from abc import ABC, abstractmethod


class Product:
    """Represents a product in the store."""

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def get_quantity(self) -> int:
        """Return the quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Set the quantity and deactivate product if quantity is zero."""
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Return whether the product is active."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self) -> str:
        """Return a string representation of the product."""
        promo_str = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promo_str}"

    def buy(self, quantity: int) -> float:
        """Purchase a quantity of the product and apply promotion if exists."""
        if quantity > self.quantity:
            raise Exception("Not enough stock available.")

        total_price = self.price * quantity
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)

        self.set_quantity(self.quantity - quantity)
        return total_price

    def set_promotion(self, promotion):
        """Set a promotion for the product."""
        self.promotion = promotion

    def get_promotion(self):
        """Get the promotion of the product."""
        return self.promotion


class NonStockedProduct(Product):
    """Represents a non-stocked product."""

    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def show(self) -> str:
        """Show the details of a non-stocked product."""
        return f"{self.name}, Price: {self.price}, Non-stocked product"


class LimitedProduct(Product):
    """Represents a product with limited purchase quantity."""

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self) -> str:
        """Show the details of a limited product."""
        return f"{self.name}, Price: {self.price}, Max Purchase Limit: {self.maximum}"

    def buy(self, quantity: int) -> float:
        """Override buy method to handle maximum purchase limit."""
        if quantity > self.maximum:
            raise Exception(f"You can only buy {self.maximum} of this product.")
        return super().buy(quantity)


class Promotion(ABC):
    """Abstract base class for promotions."""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        """Abstract method to apply promotion to a product."""
        pass


class SecondHalfPrice(Promotion):
    """Promotion: Second item at half price."""

    def apply_promotion(self, product, quantity) -> float:
        """Apply second item at half price promotion."""
        if quantity < 2:
            return product.price * quantity
        full_price_items = quantity // 2
        half_price_items = quantity - full_price_items
        return (full_price_items * product.price) + (half_price_items * product.price / 2)


class ThirdOneFree(Promotion):
    """Promotion: Buy 2, get 1 free."""

    def apply_promotion(self, product, quantity) -> float:
        """Apply buy 2, get 1 free promotion."""
        free_items = quantity // 3
        paid_items = quantity - free_items
        return paid_items * product.price


class PercentDiscount(Promotion):
    """Promotion: Percentage discount."""

    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        """Apply percentage discount promotion."""
        return product.price * quantity * (1 - self.percent / 100)
