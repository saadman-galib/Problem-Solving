t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    count = 0

    if(x == 0 or y == 0):
        print(0)
    elif(x % 3 == 0 and y % 3 == 0):
        print(0)
    elif(x % 3 == y % 3):
        print(x % 3)
    elif(max(x, y) - min(x, y) % 3 == 0):
        print(min(x, y))