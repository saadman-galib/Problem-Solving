t = int(input())

for _ in range(t):
    a = input()
    b = input()
    
    count = 0

    for i in range(len(a)):
        if a[i] == b[i]:
            count += 1
        else:
            break
   
    count = (len(a) - count) + (len(b) - count) + count + 1 if count > 0 else (len(a) - count) + (len(b) - count) + count

    print(count)

    # Not solved