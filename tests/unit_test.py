import sys

sys.path.append(r'C:\\Users\\Ondrej\\Desktop\\CI-pipeline\\CI-pipeline\\src')

from src.py import createProduct, calculateTotalPrice, askForProduct 

def test_createProduct():
    product = createProduct("Test Product", 5.5)
    assert product == {"name": "Test Product", "price": 5.5}

def test_calculateTotalPrice():
    products = [{"name": "Product 1", "price": 6}, {"name": "Product 2", "price": 3.51}]
    total = calculateTotalPrice(products)
    assert total == 9.51