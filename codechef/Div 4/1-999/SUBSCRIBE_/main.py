import math

t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    print(math.ceil(n / 6) * x)
