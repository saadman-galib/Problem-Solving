t = int(input())

for i in range(t):
    n, x, k = map(int,  input().split())
    ans = "YES" if n * x <= k else "NO"
    print(ans)