from abc import ABC, abstractmethod
import products


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
