#This program calculates the net salary of an employee after deductions
bsalary = float(input("Enter the basic salary: "))
hra=float(input("Enter the HRA (House Rent Allowance): "))
da=float(input("Enter the DA (Dearness Allowance): "))  
pf=float(input("Enter the PF (Provident Fund): "))
net_salary = bsalary + hra + da - pf
print(f"The net salary of the employee is: {net_salary}")