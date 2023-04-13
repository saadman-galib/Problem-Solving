t = int(input())

for i in range(t):
    n, a, b = map(int, input().split())
    indice_list = []
    for j in range(1, n + 1):
        indice_list.append(j)
    even_count = 0
    odd_count = 0
    for num in indice_list:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(even_count * a + odd_count * b)