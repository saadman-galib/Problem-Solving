t = int(input())

for i in range(t):
    k, x = map(int, input().split())
    ans = (k * 7) - x
    print(ans)