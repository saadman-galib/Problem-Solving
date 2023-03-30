a, b, c = map(float, input().split())

pi = 3.14159

print(f"""TRIANGULO: {(1 / 2) * a * c:.3f}
CIRCULO: {pi * (c ** 2):.3f}
TRAPEZIO: {(a + b) * (c / 2):.3f}
QUADRADO: {b ** 2:.3f}
RETANGULO: {a * b:.3f}""")