#This program is to calculate the discount and net price of a product based on its price.
price=float(input("Enter the price of the product: "))
discount=0
net_price=0
if price<=1000:
    discount=price*0.10
elif price>=1000 and price <=2000:
    discount=price*0.15
elif price>=2000 and price <=3000:
    discount=price*0.18
else:
    discount=price*0.22
net_price=price-discount
print(f"Price = {price}")
print(f"The customer has get Discount of {discount}")
print(f"The customer has to pay Net Price of {net_price}")