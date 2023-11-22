t = int(input())
frames = 24
words_per_frame = 1000

for _ in range(t):
    t = int(input())
    print(t * frames * words_per_frame)