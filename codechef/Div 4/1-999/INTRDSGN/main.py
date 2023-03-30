t = int(input())

for i in range(t):
    a, b, x, y = map(int, input().split())
    print(min(a + b, x + y))