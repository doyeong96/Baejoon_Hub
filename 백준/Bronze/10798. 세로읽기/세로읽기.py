words = [input() for i in range(5)]

for c in range(15):
    for r in range(5):
        if c < len(words[r]):
            print(words[r][c], end='')