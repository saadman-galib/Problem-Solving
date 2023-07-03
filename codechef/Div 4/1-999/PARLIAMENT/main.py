t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    print("YES" if (x * 2) >= n else "NO")