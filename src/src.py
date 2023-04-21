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

def askForProduct():
    while True:
            count = int(input("Enter the number of products to add: "))
            if count >= 0:
                break
            else:
                print("Invalid input. Please enter a positive integer.")

    products = []
    for i in range(count):
        name = input(f"Enter the name of product {i+1}: ")
        price = float(input(f"Enter the price of product {i+1}: "))
        product = createProduct(name, price)
        products.append(product)
    
    calculateTotalPrice(products)
    

askForProduct()
print('Total Price:', totalPrice)
