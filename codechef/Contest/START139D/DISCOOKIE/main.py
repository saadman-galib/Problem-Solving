t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    if(m > n):
        a = m - ((m // n) * n)
        b = (((m // n) + 1) * n) - m

        print(a if a < b else b)

    else:
        a = n - m

        print(a)