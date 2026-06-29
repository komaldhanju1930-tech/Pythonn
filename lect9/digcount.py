#This program is used to count the number of digits in a given number using while loop
n= int(input("Enter a number: "))
count = 0
while n > 0:
    n //= 10
    count += 1
print(f"The number of digits in the given number is: {count}")