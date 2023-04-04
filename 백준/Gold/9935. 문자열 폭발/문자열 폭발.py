from collections import deque

word = list(input())
bomb = input()

stack = []

m = len(bomb)
a = ""
for c in word:
    stack.append(c)
    if stack[-1] in bomb:
        if len(stack) >= m:
            for i in range(len(stack) - m, len(stack)):
                a += stack[i]
            # a = "".join(stack[-len(bomb):])
            if a == bomb:
                for _ in range(m):
                    stack.pop()
            a = ""

if stack:
    for a in stack:
        print(a, end="")
else:
    print("FRULA")
