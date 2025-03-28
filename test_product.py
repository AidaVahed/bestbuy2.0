import pytest
from products import Product

def test_create_product():
    """Test creating a normal product."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active() is True

def test_create_product_with_empty_name():
    """Test creating a product with an empty name."""
    with pytest.raises(Exception):
        Product("", price=1450, quantity=100)

def test_create_product_with_negative_price():
    """Test creating a product with a negative price."""
    with pytest.raises(Exception):
        Product("MacBook Air M2", price=-10, quantity=100)

def test_product_deactivation():
    """Test deactivation when quantity reaches 0."""
    product = Product("MacBook Air M2", price=1450, quantity=1)
    product.buy(1)
    assert product.is_active() is False
    assert product.get_quantity() == 0

def test_buying_more_than_available():
    """Test buying more than available stock."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(Exception):
        product.buy(200)
