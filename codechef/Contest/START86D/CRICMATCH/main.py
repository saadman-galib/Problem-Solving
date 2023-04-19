t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    print("YES" if (m * 6 * 6) >= n else "NO")