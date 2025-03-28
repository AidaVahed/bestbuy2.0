import pytest
import products

def test_create_valid_product():
    """Test creating a valid product."""
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active() == True

def test_create_invalid_product_empty_name():
    """Test creating a product with an empty name."""
    with pytest.raises(Exception):
        products.Product("", price=1450, quantity=100)

def test_create_invalid_product_negative_price():
    """Test creating a product with a negative price."""
    with pytest.raises(Exception):
        products.Product("MacBook Air M2", price=-10, quantity=100)

def test_create_invalid_product_negative_quantity():
    """Test creating a product with a negative quantity."""
    with pytest.raises(Exception):
        products.Product("MacBook Air M2", price=1450, quantity=-10)

def test_product_deactivation_when_quantity_reaches_zero():
    """Test that product becomes inactive when quantity reaches 0."""
    product = products.Product("MacBook Air M2", price=1450, quantity=1)
    product.buy(1)
    assert product.is_active() == False

def test_product_purchase_modifies_quantity():
    """Test that buying a product modifies its quantity."""
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    product.buy(10)
    assert product.get_quantity() == 90

def test_product_purchase_raises_exception_when_not_enough_stock():
    """Test that buying more than available stock raises an exception."""
    product = products.Product("MacBook Air M2", price=1450, quantity=10)
    with pytest.raises(Exception):
        product.buy(20)

def test_non_stocked_product():
    """Test non-stocked product behavior."""
    product = products.NonStockedProduct("Windows License", price=125)
    assert product.get_quantity() == 0
    assert product.is_active() == True
    assert product.show() == "Windows License, Price: 125, Non-stocked product"

def test_limited_product_purchase():
    """Test limited product purchase."""
    product = products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    assert product.show() == "Shipping, Price: 10, Max Purchase Limit: 1"
    assert product.buy(1) == 10
    with pytest.raises(Exception):
        product.buy(2)
