t = int(input())

for _ in range(t):
    a, b, k = map(int, input().split())

    count = 0

    while( a != b):
        if((a * k ) <= b):
            a = a * k
            count += 1
        else:
            a += 1
            count += 1

    print(count)


# Not Solved