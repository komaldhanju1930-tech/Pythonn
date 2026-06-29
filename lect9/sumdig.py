#This program calculates the sum of digits of a given number.
n=int(input("Enter a number: "))
s=0
while n>0:
    s=s+n%10
    n=n//10
print(f"Sum of digits: {s}")