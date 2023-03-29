n = int(input())

for i in range(n):
    alice, bob = map(int, input().split())

    if((alice + bob) % 2 == 0):
        print("YES")
    else:
        print("NO")