n = int(input())

for i in range(n):
    watch_time = int(input())
    if(watch_time > 24):
        print("YES")
    else:
        print("NO")