t = int(input())

for _ in range(t):
    x, y, m = map(int, input().split())
    print("YES" if (m * x) < y else "NO")