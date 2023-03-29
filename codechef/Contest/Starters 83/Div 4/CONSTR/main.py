# t = int(input())
t = 1

for i in range(t):
    global n 
    # n, u = map(str, input().split())
    n = 7
    u = 'abbbbbc'
    n = int(n)
    
    u_list = list(u)
    print(u_list)

    for j in range(n):
        if(n <= 4 or (j + 2) > n):
            break
        else:
            if(u_list[j] == u_list[j + 1] == u_list[j + 2]):
                for k in range(2):
                    u_list.pop(j)
                    print(j, n)
                n = len(u_list)
                print(u_list)
                print(j, n)
                if n%2==0:
                    j -= 1
            else:
                pass
    print("".join(u_list))