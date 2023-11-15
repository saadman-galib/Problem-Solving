t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    rated = x
    unrated = (2 * n) - x

    if(rated <= 0):
        print(0)
    else:
        while (n <= 1):
            if (unrated > 0):
                unrated -= 1
                rated -= 1
            else:
                rated -= 2
            n -= 1


        print(0 if rated < 0 else rated)