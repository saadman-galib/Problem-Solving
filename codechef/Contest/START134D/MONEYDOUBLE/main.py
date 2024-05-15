t = int(input())

for _ in range(t):
    x, y = map(int, input().split())


    for i in range(y):
        if(x < 1000):
            x += 1000
        else:
            x *= 2
            
    print(x)
