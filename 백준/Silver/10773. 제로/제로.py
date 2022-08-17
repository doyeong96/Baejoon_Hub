def push(item):
    global top
    top += 1
    stack[top] = item

def pop():
    global top
    stack[top] = 0
    top -= 1

n = int(input())
stack = [0] * n
top = -1
hap = 0
for _ in range(n):
    num = int(input())

    if num == 0:
        pop()
    else:
        push(num)
for i in stack:
    hap += i
print(hap)