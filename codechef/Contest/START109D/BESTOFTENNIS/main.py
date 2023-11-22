t = int(input())
n = 0
for _ in range(t):
    s, t = map(int, input().split())
    n = s + t + (abs(s - t) - 1)
    print(n)