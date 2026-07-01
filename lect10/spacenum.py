i = 1
while i <= 5:
    j = 1
    while j <= 5 - i:
        print("_", end="")
        j += 1

    j = 1
    while j <= i:
        print(j, end="")
        j += 1

    j = i - 1
    while j >= 1:
        print(j, end="")
        j -= 1     
    print()
    i += 1