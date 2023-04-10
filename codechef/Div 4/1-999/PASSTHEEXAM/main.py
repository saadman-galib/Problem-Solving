t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    print("PASS" if (a >= 10 and b >= 10 and c >= 10) and (a + b + c >= 100) else "FAIL")