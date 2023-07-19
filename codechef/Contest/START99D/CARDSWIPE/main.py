t = int(input())

for _ in range(t):
    n = int(input())
    swipe_array = list(map(int, input().split()))
    new_array = []
    count = 0

    for i in range(n):
        if swipe_array[i] in new_array:
            # if swipe_array.count(swipe_array[i]) > 1:
            count -= 1
            new_array.remove(swipe_array[i])
        else:
            count += 1
            new_array.append(swipe_array[i])
    print(count)


    # Not Solved