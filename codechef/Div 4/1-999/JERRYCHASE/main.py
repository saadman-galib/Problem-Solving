n = int(input())

for i in range(n):
    jerry_speed, tom_speed = map(int, input().split())
    if(tom_speed > jerry_speed):
        print("YES")
    else:
        print("NO")