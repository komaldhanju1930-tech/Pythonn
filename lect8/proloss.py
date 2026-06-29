#This program calculates the profit or loss made by the owner of a shop based on the sale price and cost price of an item.
saleprice=float(input("Enter the sale price: "))
costprice=float(input("Enter the cost price: "))
if costprice>saleprice :
    profit=costprice-saleprice
    print(f"The owner has made a profit of {profit}")
else:
    loss=saleprice-costprice
    print(f"The owner has incurred a loss of {loss}")