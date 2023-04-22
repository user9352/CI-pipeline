import sys

sys.path.append('/home/runner/work/CI-pipeline/CI-pipeline/src')

from src import *

def test_askForProduct():
    count = 2
    names = ["Product 1", "Product 2"]
    prices = [6, 3.51]
    total_price = askForProduct(count, names, prices)
    assert total_price == 9.51, "Total price is not calculated correctly"

def test_createProduct():
    product = createProduct("Test Product", 5.5)
    assert product == {"name": "Test Product", "price": 5.5}

def test_calculateTotalPrice():
    products = [{"name": "Product 1", "price": 6}, {"name": "Product 2", "price": 3.51}]
    total = calculateTotalPrice(products)
    assert total == 9.51