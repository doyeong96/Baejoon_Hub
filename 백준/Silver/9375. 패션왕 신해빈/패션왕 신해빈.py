for _ in range(int(input())):
    n = int(input())
    wear = {}
    for i in range(n):
        a, b = input().split()
        if b in wear:
            wear[b] += 1
        elif b not in wear:
            wear[b] = 1
    day = 1
    for val in wear.values():
        day *= (val+1)
    print(day-1)
