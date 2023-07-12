a, b, x, y = map(int, input().split())

messi_points = (a * 2) + (b * 1)
ronaldo_points = (x * 2) + (y * 1)

if messi_points > ronaldo_points:
    print("Messi")
elif messi_points < ronaldo_points:
    print("Ronaldo")
else:
    print("Equal")
