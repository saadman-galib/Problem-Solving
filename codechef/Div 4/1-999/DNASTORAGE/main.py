t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    new_str = ''

    for i in range(0, n, 2):
         
        if (s[i] + s[i + 1] == '00'):
            new_str += 'A'
        elif(s[i] + s[i + 1] == '01'):
            new_str += 'T'
        elif(s[i] + s[i + 1] == '10'):
            new_str += 'C'
        else:
            new_str += 'G'
    
    print(new_str)