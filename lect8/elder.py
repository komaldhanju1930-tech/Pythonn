#This program is to find the eldest person among Ram, Shyam and Mohan
ram_age=int(input("Enter the age of ram: "))
shyam_age=int(input("Enter the age of shyam: "))
mohan_age=int(input("Enter the age of mohan: "))
if ram_age>shyam_age :
    if ram_age>mohan_age:
        print("Ram is the eldest")
    else :
        print("Mohan is the eldest")
else :
    if shyam_age>mohan_age:
        print("Shyam is the eldest")
    else :
        print("Mohan is the eldest")            