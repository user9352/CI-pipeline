import sys

sys.path.append('/home/runner/work/CI-pipeline/CI-pipeline/src')


def test_askForProduct(mocker):
    # Mock the function using mocker
    askForProduct = mocker.patch('src.askForProduct.count')
    askForProduct.return_value = "Mocked result"

    # Call the function being tested
    result = askForProduct()

    # Assert that the mock function was called
    askForProduct.assert_called_once()

    # Assert the result
    assert result == "Mocked result"
    
from src import *

def test_createProduct():
    product = createProduct("Test Product", 5.5)
    assert product == {"name": "Test Product", "price": 5.5}

def test_calculateTotalPrice():
    products = [{"name": "Product 1", "price": 6}, {"name": "Product 2", "price": 3.51}]
    total = calculateTotalPrice(products)
    assert total == 9.51