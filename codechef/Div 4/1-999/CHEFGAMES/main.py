t = int(input())

for _ in range(t):
    r1, r2 ,r3, r4 = map(int, input().split())
    print("IN" if (r1 + r2 + r3 + r4) == 0 else "OUT")