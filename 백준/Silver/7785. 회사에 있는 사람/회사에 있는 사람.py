li = []
for _ in range(int(input())):
    a,b = input().split()
    if b == 'enter':
        li.append(a)
    else:
        li.pop(li.index(a))
li.sort(reverse=True)
for i in range(len(li)):
    print(li[i])

