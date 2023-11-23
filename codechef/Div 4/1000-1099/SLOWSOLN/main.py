t = int(input())

for _ in range(t):
    maxT, maxN, sumN = map(int, input().split())
    result = 0

    while(True):
        if sumN <= maxN:
            break
        else:

            result += maxN ** 2
            sumN -= maxN
        maxT -= 1

    print(result)

#not solved