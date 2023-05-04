t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr_set = set(arr)
    new_arr = list(arr_set)
    new_arr.sort()
    print(new_arr[-1] + new_arr[-2])