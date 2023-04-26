t = int(input())

for _ in range(t):
    x = int(input())
    y = x // 10
    x %= 10
    y = y if x < 5 else y + 1
    y *= 10
    print(100 - y)
