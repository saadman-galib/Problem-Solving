t = int(input())

for _ in range(t):
    x, y, z = map(int, input().split())

    if(x > y and x > z):
        print("Setter")
    elif(y > x and y > z):
        print("Tester")
    else:
        print("Editorialist")