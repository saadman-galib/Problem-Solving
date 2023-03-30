money = float(input())
money_list = [100, 50, 20, 10, 5, 2]
moedas_list = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')

for i in money_list:
    value = money // i
    print(f"{int(value)} nota(s) de R$ {i:.2f}")
    money -= value * i

print('MOEDAS:')

for j in moedas_list:
    value = money // j
    print(f"{int(value)} moeda(s) de R$ {j:.2f}")
    money -= value * j
