#This program takes a number input from the user and prints the corresponding day of the week.
day=int(input("Enter the day of the week (1-7): "))
if day==1:
    print("Monday")
elif day==2:
    print("Tuesday")
elif day==3:
    print("Wednesday")
elif day==4:
    print("Thursday")
elif day==5:
    print("Friday")
elif day==6:
    print("Saturday")
elif day==7:
    print("Sunday")
else:
    print("Invalid day of the week. Please enter a number between 1 and 7.")