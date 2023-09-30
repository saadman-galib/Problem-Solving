t = int(input())

for _ in range(t):
    a, b , c = map(int, input().split())

    while (b > 0):
        a -= c
        b -= 1
    
    print("YES" if a <= 0 else "NO")
    