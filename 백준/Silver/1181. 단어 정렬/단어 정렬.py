n = int(input())
words = [input() for _ in range(n)]
words = list(set(words))
words = sorted(words)
words.sort(key=lambda x: len(x))
for words in words:
    print(words)
