t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    if (y < x):
        print("NO")
    elif(x + 200 < y):
        print("NO")
    else:
        print("YES")
