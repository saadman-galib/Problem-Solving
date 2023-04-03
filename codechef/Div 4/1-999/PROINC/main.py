for _ in range(int(input())):
    x, y = map(int, input().split())
    new_x = x * 1.1
    print(int(new_x - (x - y)))