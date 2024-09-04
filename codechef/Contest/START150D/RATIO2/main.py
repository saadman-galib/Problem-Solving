t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    if(x == y * 2 or y == x * 2):
        print(0)
    else:
        a = abs((max(x, y) / 2) - min(x, y))
        b = abs((min(x, y) / 2) - max(x, y))

        if(int(a) == a and int(b) == b):
            print(int(min(a, b)))
        elif(int(a) == a):
            print(a)
        else:
            print(b)
    #not solved
    