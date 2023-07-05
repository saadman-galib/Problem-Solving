t = int(input())

for _ in range(t):
    array = list(map(int, input().split()))

    a = array[:len(array) // 2]
    b = array[len(array) // 2:]

    a.sort(reverse=True)
    b.sort(reverse=True)

    if((a[0] + a[1]) == (b[0] + b[1])):
        print("Tie")
    elif((a[0] + a[1]) > (b[0] + b[1])):
        print("Alice")
    else:
        print("Bob")