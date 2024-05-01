n = int(input())
for i in range(n):
    s = input()
    words = s.split()
    
    for i, word in enumerate(words):
        if not word.isupper():
            title = word[0].upper() + word[1:].lower()
            words[i] = title
        else:
            words[i] = word

    print(' '.join(words))