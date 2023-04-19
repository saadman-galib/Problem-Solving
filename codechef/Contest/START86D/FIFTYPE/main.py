t = int(input())

for _ in range(t):
    n = int(input())
    time = 0

    while n != 50:
        if n > 50:
            while n > 50:
                n -= 3
                time += 1
        elif n < 50 and (50 - n) % 2 != 0:
            while (50 - n) % 2 != 0:
                n -= 3
                time += 1
        elif n < 50 and (50 - n) % 2 == 0:
            while n != 50:
                n += 2
                time += 1
    
    print(time)