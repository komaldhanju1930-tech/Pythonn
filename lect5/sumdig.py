#This program calculates the sum of digits of a given number
num = int(input("Enter a number: "))
s=0
s=s+num%10
num=num//10
s=s+num%10
num=num//10
s=s+num%10
num=num//10
s=s+num%10
num=num//10
print(f"The sum of digits of the given number is: {s}")