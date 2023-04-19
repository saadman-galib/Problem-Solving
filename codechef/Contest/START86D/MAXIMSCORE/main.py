t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(abs(a[1] - a[0]))

# not solved