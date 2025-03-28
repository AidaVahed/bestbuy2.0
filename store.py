from typing import List


class Store:
    def __init__(self, products: List['Product']):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self) -> List['Product']:
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            if product.get_quantity() < quantity:
                raise Exception(f"Not enough {product.name} in stock")
            total_price += product.buy(quantity)
        return total_price
