import sys

sys.path.append('/home/runner/work/CI-pipeline/CI-pipeline/src')

from src import *

def test_askForProduct(mocker, capsys, monkeypatch):
    # Mock user input
    user_input = "2\nProduct 1\n6\nProduct 2\n3.51\n"
    monkeypatch.setattr('builtins.input', lambda _: user_input)

    # Call the function being tested
    askForProduct()

    # Capture the printed output
    captured = capsys.readouterr()

    # Assert the expected output
    assert captured.out == "Total Price: 9.51\n"

def test_createProduct():
    product = createProduct("Test Product", 5.5)
    assert product == {"name": "Test Product", "price": 5.5}

def test_calculateTotalPrice():
    products = [{"name": "Product 1", "price": 6}, {"name": "Product 2", "price": 3.51}]
    total = calculateTotalPrice(products)
    assert total == 9.51