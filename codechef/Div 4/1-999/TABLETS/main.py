t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    print("YES" if 3 * x <= y else "NO")