t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    if(x == 0 and y == 0):
        print("NO")
    else:
        print("YES" if (x == y) else "NO")