for _ in range(int(input())):
    n = int(input())
    t = list(map(int, input().split()))
    has_sequence = False
    for i in range(1, n):
        for j in range(n):
            if(t[j] == i):
                has_sequence = True
                break
        
    print("YES" if has_sequence else "NO")