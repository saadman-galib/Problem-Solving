t = int(input())

for i in range(t):
    a, b, c = map(int, input().split())
    min_num = min(a, b, c)
    max_num = max(a, b, c)

    if(min_num == a and max_num == b):
        print(c)
    elif(min_num == a and max_num == c):
        print(b)
    elif(min_num == b and max_num == c):
        print(a)
    elif(min_num == b and max_num == a):
        print(c)
    elif(min_num == c and max_num == a):
        print(b)
    elif(min_num == c and max_num == b):
        print(a)