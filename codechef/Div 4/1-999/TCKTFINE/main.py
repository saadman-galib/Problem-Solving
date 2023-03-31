t = int(input())

for i in range(t):
    x, p, q = map(int, input().split())
    ans = x * (p - q)
    print(ans)