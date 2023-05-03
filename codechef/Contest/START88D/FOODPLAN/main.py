t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = n - (n * 0.1)

    if(a < m):
        print("ONLINE")
    elif(m < a):
        print("DINING")
    else:
        print("EITHER")