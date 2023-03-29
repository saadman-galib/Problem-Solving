t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    if(n + 1 <= k):
        print("YES")
    else:
        print("NO")