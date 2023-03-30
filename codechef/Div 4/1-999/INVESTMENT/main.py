t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    ans = "YES" if x >= y * 2 else "NO"
    print(ans)