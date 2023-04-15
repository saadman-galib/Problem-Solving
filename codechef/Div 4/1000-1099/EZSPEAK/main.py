t = int(input())

for _ in range(t):
    n = int(input())
    s = input().lower()
    s = s.strip()

    vowels = ['a', 'e', 'i', 'o', 'u']
    consonant = 0
    is_hard = False
    
    if(n < 4):
        print("YES")
    else:
        for i in range(n):
            if s[i] not in vowels:
                consonant += 1
                if(consonant >= 4):
                    is_hard = True
                    break
            else:
                consonant = 0

        print("NO" if is_hard else "YES")
