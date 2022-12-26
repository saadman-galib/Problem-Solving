money = int(input())
money_list = [100, 50, 20, 10, 5, 2, 1]

print(money)

for i in money_list:
    value = money // i
    print(f"{value} nota(s) de R$ {i},00")
    money -= value * i