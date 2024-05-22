t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    count_0 = 0
    count_1 = 0

    if(n == 1):
        print(0)
    else:
        for i in range(n):
            if(i != 0):
                if s[i - 1] == '0' and s[i] == '1':
                    count_0 += 1
            elif(s[0] == '1'):
                count_0 += 1
        
        for j in range(n):
            if(j != 0):
                if s[j - 1] == '1' and s[j] == '0':
                    count_1 += 1
            elif(s[0] == '0'):
                count_1 += 1

        print(min(count_0, count_1))