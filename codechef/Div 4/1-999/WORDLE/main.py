t = int(input())

for _ in range(t):
    s = input()
    t = input()

    for  i in range(len(s)):
        if s[i] == t[i]:
            print("G", end="")
        else:
            print("B", end="")

    print()