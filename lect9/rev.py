#This program is used to reverse a given number using while loop
n=int(input("Enter a number: "))
rev=0
digit=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print(f"The reverse of the given number is: {rev}")