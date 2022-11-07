words = list(input())
right = []

n = int(input())
cursor = len(words)
# print(word)
for _ in range(n):
    cmd = input().split()
    # L
    if cmd[0] == 'L' and words:
        word = words.pop()
        right.append(word)
    # D
    if cmd[0] == 'D' and right:
        word = right.pop()
        words.append(word)
    # B
    if cmd[0] == 'B' and words:
        words.pop()
    # P
    if cmd[0] == 'P':
        words.append(cmd[1])

# print(words)
right.reverse()
# print(right)
new_words = words + right
print(''.join(new_words))
