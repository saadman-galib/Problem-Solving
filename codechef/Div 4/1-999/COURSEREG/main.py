for _ in range(int(input())):
    n, m , k = map(int, input().split())
    print("YES" if (n + k) <= m else "NO")    