#This program calculates the tax to be paid by a person based on their income.
income=float(input("Enter income of a person: "))
if income<=1200000:
    tax=0
elif income>=1200000 and income <=1600000:
    tax=income*0.05
elif income>=1600000 and income <=2000000:
    tax=income*0.10
elif income>=2000000 and income <=2400000:
    tax=income*0.15
elif income>=2400000 :
    tax=income*0.20
print(f"Tax to be paid = {tax}")