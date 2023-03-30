t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    print((x - y) if x > y else 0)