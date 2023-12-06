for _ in range(int(input())):
    x, y, z = map(int, input().split())
    print("YES" if(z > (x * y) / 2) else "NO")