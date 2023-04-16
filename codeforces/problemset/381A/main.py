n = int(input())
a = list(map(int, input().split()))

sereja = 0
dima = 0

for i in range(n):
    if i % 2 == 0:
        if a[0] > a[-1]:
            sereja += a[0]
            a.pop(0)
        else:
            sereja += a[-1]
            a.pop(-1)
    else:
        if a[0] > a[-1]:
            dima += a[0]
            a.pop(0)
        else:
            dima += a[-1]
            a.pop(-1)

print(f"{sereja} {dima}")