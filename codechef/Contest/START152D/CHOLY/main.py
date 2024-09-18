x, y, z = map(int, input().split())

if(x + y + z ==4):
    print("YES" if x > z else "NO")
else:
    if(z > x):
        count = 4 - (z - x)
    print("YES" if (z - x) < (x + y + z) else "NO")

# not solved