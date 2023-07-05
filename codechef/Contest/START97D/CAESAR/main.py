alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

s_array = []
t_array = []
u_array = []

k = 0

for _ in range(int(input())):
    n = int(input())
    s = list(str(input()))
    # t = list(str(input()))
    # u = list(str(input()))
    # print(alphabets.index(s[0]))
    

    

    s.reverse()
    # # t.reverse()
    # # u.reverse()

    s.append(s[0])

    print(s)
    
    for i in range(n):
        s_array.append(alphabets.index(s[i]))
        s_array.append(s_array[i] + 26)

    for i in range(n):
        t_array.append(alphabets.index(s[i]))
        t_array.append(s_array[i] + 26)

    for i in range(n):
        if(i == 0):
            k = alphabets.index(s[i]) - alphabets.index(s[i + 1])
        else:
            if (k == l or l == l):
                l = alphabets.index(s[i]) - alphabets.index(s[i + 1])

    
    print(s_array)


# not solved