t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    prev = ''
    count = 0

    for i in range(n):
        if(prev != ''):
            if(s[i] == prev):
                prev = ''
            else:
                count += 1
                prev = s[i]
        else:
            prev = s[i]
            count += 1
    print(count)
        

