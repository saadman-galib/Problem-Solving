t = int(input())

for i in range(t):
    n, x, y = map(int, input().split())
    
    if(n <= (x * y)):
        print("YES")
    else:
        print("NO")