t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    print("YES" if (((x ** 4) + 4 * (y ** 2)) == 4 * (x ** 2) * y) else "NO")