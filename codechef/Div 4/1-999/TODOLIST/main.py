t = int(input())

for _ in range(t):
    n = int(input())
    problems = list(map(int, input().split()))
    greater_than_1000 = 0

    for i in range(n):
        if(problems[i] >= 1000):
            greater_than_1000 += 1
    print(greater_than_1000)