n = int(input())

while(n):
    income = int(input())
    tax = income if income <= 100 else income - 10
    print(tax)
    n -= 1