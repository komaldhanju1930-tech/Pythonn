#This program determines whether a student has passed or failed.
m1=float(input("Enter the marks of 1st subject: "))
m2=float(input("Enter the marks of 2nd subject: "))
m3=float(input("Enter the marks of 3rd subject: "))
m4=float(input("Enter the marks of 4th subject: "))
m5=float(input("Enter the marks of 5th subject: "))
total=m1+m2+m3+m4+m5
percentage=(total/500)*100
print(f"The total marks obtained by the student is: {total}")
print(f"The percentage of marks obtained by the student is: {percentage:.2f}%")
if percentage>=40:
    print("The student has passed.")
else:
    print("The student has failed.")