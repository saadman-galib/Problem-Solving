numbers = []

t = int(input())

for i in range(t):
    numbers.append(int(input()))

numbers.sort()
for j in range(len(numbers)):
    print(numbers[j])