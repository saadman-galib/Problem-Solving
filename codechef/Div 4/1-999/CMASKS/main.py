t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    x_cost = x * 100
    y_cost = y * 10
    if x_cost < y_cost:
        print("Disposable")
    elif x_cost > y_cost:
        print("Cloth")
    else:
        print("Cloth")