totalPrice = 0

def createProduct(name, price):
    return {
        "name": name,
        "price": price
    }

def calculateTotalPrice(products):
    global totalPrice
    for product in products:
        totalPrice += product["price"]
    return totalPrice

def askForProduct(count, names, prices):
    products = []
    for i in range(count):
        name = names[i]
        price = prices[i]
        product = createProduct(name, price)
        products.append(product)
    
    return calculateTotalPrice(products)

#count = 2
#names = ["Product 1", "Product 2"]
#prices = [6, 3.51]
#total_price = askForProduct(count, names, prices)
#print('Total Price:', total_price)