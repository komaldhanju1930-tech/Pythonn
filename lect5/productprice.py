#This program will calculate the price of wanted number of a product
product_price = float(input("Enter the price of the product: "))
quantity = int(input("Enter the quantity of the product: "))
total_price = product_price * quantity
print(f"The total price of {quantity} units of the product is: {total_price}")