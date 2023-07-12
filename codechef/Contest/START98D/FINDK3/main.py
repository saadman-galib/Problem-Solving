t = int(input())

for _ in range(t):
    x = list(map(int, input().split()))

    ans_found = False

    x.reverse()
    x.extend(x)

    for i in range(3):
        b = x[i]
        a = x[i + 1] * x[i + 2]

        if (a % b == 0):
            ans_found = True
            break
        
    print("-1" if (ans_found == False) else f"{a} {b}")
        