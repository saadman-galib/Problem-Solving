t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    s = input().split()

    ind = map(int, input().split())

    c = input()

    for i in ind:
        s[i -1 ] = c[i]

    print("".join(s))

    #Not Solved