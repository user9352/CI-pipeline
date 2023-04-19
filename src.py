# Function that creates and returns a product object
totalPrice = 0

def createProduct(name, price):
    return {
        "name": name,
        "price": price
    }

# Function that calculates and returns the total price of products in a list
def calculateTotalPrice(products):
    global totalPrice
    for product in products:
        totalPrice += product["price"]
    return totalPrice

# Function that asks the user how many products to add
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
    

# Example usage
askForProduct()
print('Total Price:', totalPrice)
