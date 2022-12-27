import math

a, b, c = map(float, input().split())

if(a != 0):
    if(((b ** 2) - 4 * a * c) >= 0):
        root1 = (-b + math.sqrt(((b ** 2) - 4 * a * c))) / (2 * a)
        root2 = (-b - math.sqrt(((b ** 2) - 4 * a * c))) / (2 * a)
        print(f"R1 = {root1:.5f}\nR2 = {root2:.5f}")
    else:
        print("Impossivel calcular")        
else:
    print("Impossivel calcular")