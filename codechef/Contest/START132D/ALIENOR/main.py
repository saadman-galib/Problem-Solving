t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    array_2d = []
    
    for i in range(n):
        array_2d.append([*input()])
        array_2d[-1] = [int(i) for i in array_2d[-1]]

    print(n, k, array_2d)

# Not Solved