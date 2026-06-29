#This program calculates the daily wage of a worker based on the number of hours worked. The wage is calculated as follows:
workhr=int(input("Enter the number of hours worked: "))
if workhr == 8:
    wage = 250
elif workhr > 8 and workhr <= 10:
    wage = 250 + (workhr - 8) * 50
elif workhr > 10 and workhr <= 12:
    wage = 250 + (2 * 50) + (workhr - 10) * 75
elif workhr > 12 and workhr <= 14:
    wage = 250 + (2 * 50) + (2 * 75) + (workhr - 12) * 100
else:
    wage = "Invalid working hour"
print(f"Daily Wage = {wage}")      