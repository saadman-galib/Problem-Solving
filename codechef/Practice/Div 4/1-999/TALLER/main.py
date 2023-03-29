t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print("A" if a > b else "B")