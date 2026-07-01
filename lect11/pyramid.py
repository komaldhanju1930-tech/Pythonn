for i in range(1,6):
    for j in range(5,i,-1): #space
        print(f"-", end="")
    print(f"*",end="")
    for k in range(1,i):
        print(f"-*", end="")
    print()