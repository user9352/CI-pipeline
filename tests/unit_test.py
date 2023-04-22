import sys

sys.path.append('/home/runner/work/CI-pipeline/CI-pipeline/src')

from src import *

@pytest.mark.parametrize("user_input, expected_output", [("2\nProduct 1\n6\nProduct 2\n3.51\n", "Total Price: 9.51\n")])
def test_askForProduct(mocker, capsys, user_input, expected_output):
    # Mock user input
    mocker.patch('builtins.input', side_effect=user_input)

    # Call the function being tested
    askForProduct()

    # Capture the printed output
    captured = capsys.readouterr()

    # Assert the expected output
    assert captured.out == expected_output

def test_createProduct():
    product = createProduct("Test Product", 5.5)
    assert product == {"name": "Test Product", "price": 5.5}

def test_calculateTotalPrice():
    products = [{"name": "Product 1", "price": 6}, {"name": "Product 2", "price": 3.51}]
    total = calculateTotalPrice(products)
    assert total == 9.51