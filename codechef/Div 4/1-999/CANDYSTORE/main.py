t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    rupee_1 = x * 1 if y > x else y * 1
    rupee_2 = (y - x) * 2 if y > x else 0
    total_sold = rupee_1 + rupee_2
    print(total_sold)