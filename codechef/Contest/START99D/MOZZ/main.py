import math

t = int(input())

for _ in range(t):
    x, y, r = map(int, input().split())
    extra_sticks = r // 30
    x += extra_sticks
    print(math.ceil(x / y))