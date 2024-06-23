t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    array_2d = []

    for i in range(n):
        array_2d.append(list(map(int, input().split())))
    
    print(n, m, array_2d)

    #Not Solved