#This program reverses a given number
n=int(input("enter value"))
rev=0
rev=rev+n%10*1000
n=n//10
rev=rev+n%10*100
n=n//10
rev=rev+n%10*10
n=n//10
rev=rev+n%10
n=n//10
print(f"The reverse of the given number is: {rev}")