#This program calculates the total fare for a group of passengers based on their age
children = int(input("Enter number of children: "))
youngs = int(input("Enter number of youngs: "))
olds = int(input("Enter number of olds: "))

fare_children = children * 450
fare_youngs = youngs * 650
fare_olds = olds * 500

total_fare = fare_children + fare_youngs + fare_olds
print(f"the fare of child is {fare_children} \nthe fare of young is {fare_youngs} \n the fare of old {fare_olds} \n the total fare is {total_fare}")