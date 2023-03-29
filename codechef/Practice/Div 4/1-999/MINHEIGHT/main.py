t = int(input())

for i in range(t):
    h, x = map(int, input().split())
    print("YES" if h >= x else "NO")