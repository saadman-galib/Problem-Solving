t = int(input())

for i in range(t):
    s = input()
    s = s.lower()
    if s == "b":
        print("BattleShip")
    elif s == "c":
        print("Cruiser")
    elif s == "d":
        print("Destroyer")
    elif s == "f":
        print("Frigate")