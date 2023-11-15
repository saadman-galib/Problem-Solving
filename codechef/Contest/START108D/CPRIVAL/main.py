r1, r2 = map(int, input().split())
d1, d2 = map(int, input().split())

if(r1 + d1 > r2 + d2):
    print("Dominater")
else:
    print("Everule")