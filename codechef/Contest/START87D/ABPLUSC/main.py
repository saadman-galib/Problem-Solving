t = int(input())

for _ in range(t):
    x = int(input())
    a = b = c = 1
    
    if(x > 1):
        for i in range(1, x): # c
            for j in range(1, x):  # a
                for k in range(1, x):   # b
                    if(j * k + i) == x:
                        a = j
                        b = k
                        c = i
                        break
                break
            break

        print(f"{a} {b} {c}")

    else:
        print(-1)
    
# not solved