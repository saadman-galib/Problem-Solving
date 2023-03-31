t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    if(x > y):
        print("SECOND")
    elif(x < y):
        print("FIRST")
    else:
        print("ANY")