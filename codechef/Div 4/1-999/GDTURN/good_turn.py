n = int(input())

for i in range(n):
    dice_1, dice_2 = map(int, input().split())
    if(dice_1 + dice_2 > 6):
        print("YES")
    else:
        print("NO")