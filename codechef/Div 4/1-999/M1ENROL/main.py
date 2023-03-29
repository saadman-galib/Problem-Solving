n = int(input())

for i in range(n):
    x, y = map(int, input().split())

    extra_seats = y - x if (y - x > 0) else 0;
    print(extra_seats)