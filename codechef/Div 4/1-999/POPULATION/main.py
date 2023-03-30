t = int(input())

for i in range(t):
    x, y, z = map(int, input().split())
    ans = x - y + z
    print(ans)