n = int(input())

while(n):
    f = int(input())
    is_audible = "NO" if (f < 67 or f > 45000) else "YES"
    print(is_audible)
    n -= 1