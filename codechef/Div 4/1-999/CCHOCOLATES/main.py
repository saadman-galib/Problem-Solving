t = int(input())

for i in range(t):
    x, y, z = map(int, input().split())
    print((x * 5 + y * 10) // z)