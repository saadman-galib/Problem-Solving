import math

t = int(input())
n = list(map(int, input().split()))

for i in range(t):
    value = n[i]
    value_bool = False

    for i in range(2, value + 1):
        if i ** i == value:
            value_bool = True
            break/

    if value_bool:
        print("yes")
    else: 
        print("no")
    