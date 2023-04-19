t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))

    temp_a = a.copy()
    a = []
    b = []

    for i in range(len(temp_a)):
        if i % 2 == 0:
            a.append(temp_a[i])
        else:
            b.append(temp_a[i])
    
    if set((a[0], b[0])) == set((a[1], b[1])):
        print(1)
    elif set((a[0], b[0])) == set((a[2], b[2])):
        print(2)
    else:
        print(0)

    