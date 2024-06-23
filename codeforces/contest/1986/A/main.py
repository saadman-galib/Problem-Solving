t = int(input())

for _ in range(t):
    x1, x2, x3 = map(int, input().split())

    a1 = abs(x1 - x2) + abs(x2 - x2) + abs(x3 - x2)
    a2 = abs(x1 - x2) + abs(x1 - x1) + abs(x3 - x1)
    a3 = abs(x1 - x3) + abs(x3 - x3) + abs(x2 - x3)

    print(min(a1, a2, a3))