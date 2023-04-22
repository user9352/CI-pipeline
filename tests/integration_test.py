import sys

sys.path.append('/home/runner/work/CI-pipeline/CI-pipeline/src')

from src import *

def test_askForProduct():
    count = 2
    names = ["Product 1", "Product 2"]
    prices = [6, 3.51]
    total_price = askForProduct(count, names, prices)
    assert total_price == 11