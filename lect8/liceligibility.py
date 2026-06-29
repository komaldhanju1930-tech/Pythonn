#This program checks if a person is eligible for life insurance based on their age.
age=int(input("Enter your age: "))
if age>=18:
    if age<=45:
        print("You are eligible for life insurance.")
    else :
        print("You are not eligible for life insurance.")
else :
    print("You should be at least 18 years old to be eligible for life insurance.")   