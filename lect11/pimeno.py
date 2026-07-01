n=int(input("Enter a number:")) 
i=2
while i<n:
    if n%i==0:
        break
    i+=1
if n==i:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")