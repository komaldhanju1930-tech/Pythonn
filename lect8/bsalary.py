#
salary=float(input("Enter the salary: "))
if salary < 10000 :
    HRA=0.10*salary
    DA=0.90*salary
else :
    HRA=0.20*salary
    DA=0.95*salary

print(f"Basic Salary = {salary}")
print(f"HRA = {HRA}")
print(f"DA = {DA}")
net_salary=salary+HRA+DA
print(f"The net salary of the employee is {net_salary}")