#This program calculates the net price of a book after applying a discount
bookprice=int(input("enter price of book"))
discount=int(input("enter discount"))
disprice=(bookprice*discount)/100
netprice=bookprice-disprice
print(f"the net price is {netprice} \nthe discount price is {disprice} ")