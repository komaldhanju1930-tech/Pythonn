#This program calculates the sum of numbers from 1 to a given number.
n=int(input("Enter a number: "))
s=0
while n>0:
    s=s+n
    n-=1
print(f"Sum of numbers: {s}")