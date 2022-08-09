T = int(input())
for i in range(1, T+1):
    word = input()
    if word == word[::-1]:
        print('#{0} 1'.format(i))
    else:
        print('#{0} 0'.format(i))
