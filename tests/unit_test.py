import sys

sys.path.append('/home/runner/work/CI-pipeline/CI-pipeline/src')

from src import createProduct, calculateTotalPrice

def test_createProduct():
    product = createProduct("Test Product", 3.51)
    assert product == {"name": "Test Product", "price": 3.51}

def test_calculateTotalPrice():
    products = [{"name": "Product 1", "price": 6}, {"name": "Product 2", "price": 3.51}]
    total = calculateTotalPrice(products)
    assert total == 9.51