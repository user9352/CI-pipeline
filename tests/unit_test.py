import sys

sys.path.append('/home/runner/work/CI-pipeline/CI-pipeline/src')

from src import *

def test_askForProduct(mocker):
    # Mock the function using mocker
    mocked_askForProduct = mocker.patch('src.askForProduct')
    mocked_askForProduct.return_value = 1

    # Call the function being tested
    result = mocked_askForProduct()

    # Assert that the mock function was called
    mocked_askForProduct.assert_called_once()

    # Assert the result
    assert result == 1

def test_createProduct():
    product = createProduct("Test Product", 5.5)
    assert product == {"name": "Test Product", "price": 5.5}

def test_calculateTotalPrice():
    products = [{"name": "Product 1", "price": 6}, {"name": "Product 2", "price": 3.51}]
    total = calculateTotalPrice(products)
    assert total == 9.51