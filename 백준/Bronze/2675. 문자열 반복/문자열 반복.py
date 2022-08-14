n = int(input())

for _ in range(n):
    num, letter = map(str, input().split())

    num = int(num)
    letter = list(letter)
    for i in range(len(letter)):
        dap = num * letter[i]
        print(dap, end='')
    print()