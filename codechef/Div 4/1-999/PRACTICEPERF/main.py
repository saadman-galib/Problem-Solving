problems = list(map(int, input().split()))
greater_than_10 = 0
for i in problems:
    if(i >= 10):
        greater_than_10 += 1
    
print(greater_than_10)
