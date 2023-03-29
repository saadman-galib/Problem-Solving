n = int(input())

for i in range(n):
    x = int(input())

    if(x < 3):
        print("LIGHT")
    elif(x < 7):
        print("MODERATE")
    else:
        print("HEAVY")
