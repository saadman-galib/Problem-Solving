t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    n = 10
    price = 0

    while(n > 1):
        if(n == 2):
            price += x
            n -= 2
        else:
            if (x * 2 <= y):
                price += x
                n -= 2
            else:
                price += y
                n -= 4
    
    print(price)
