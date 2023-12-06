t = int(input())

for _ in range(t):
    n = int(input())
    x = 0
    y = 0
    is_possible = False

    while(2 * x < n):
        x += 1

        
        if((2 * x + 7 * y) == n):
            is_possible == True
    print("YES" if is_possible else "NO" )    