s = input()

upper = 0
lower = 0

upper_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lower_letters = list("abcdefghijklmnopqrstuvwxyz")

for i in s:
    if i in upper_letters:
        upper += 1
    else:
        lower += 1

if upper > lower:
    print(s.upper())
else:
    print(s.lower())