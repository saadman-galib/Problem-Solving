n = int(input())

for i in range(n):
    alice, bob, charlie = map(int, input().split())

    if alice > bob and alice > charlie:
        print("Alice")
    elif bob > alice and bob > charlie:
        print("Bob")
    else:
        print("Charlie")