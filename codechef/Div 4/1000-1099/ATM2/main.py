t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = ''

    for i in range(n):
        ans += '1' if (k - a[i]) >= 0 else '0'
        if (k - a[i]) >= 0:
            k -= a[i]
    
    print(ans)

