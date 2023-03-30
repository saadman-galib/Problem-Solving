a, b, c = map(int, input().split())

ab = (a + b + abs(a - b)) / 2

majorAB = int((ab + c + abs(ab - c)) / 2)

print(f"{majorAB} eh o maior")