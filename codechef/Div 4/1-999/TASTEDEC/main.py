n = int(input())

for i in range(n):
    chocolate, candy = map(int, input().split())
    chocolate_tastiness = chocolate * 2
    candy_tastiness = candy * 5
    if(chocolate_tastiness > candy_tastiness):
        print("Chocolate")
    elif(candy_tastiness > chocolate_tastiness):
        print("Candy")
    else:
        print("Either")