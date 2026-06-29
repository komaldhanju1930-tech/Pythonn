#This program is used to print factorial of a number using while loop
n = int(input("Enter a number: "))
fact = 1
while n > 0:
    fact *= n
    n -= 1
print(f"The factorial of the given number is:  {fact}")