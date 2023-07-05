import sys

# sys.stdin = open("sample.txt", 'r')
input = sys.stdin.readline

w = input().strip()
s = set()
for i in range(len(w)):
    for j in range(i,len(w)):
        # a = w[i:j+1]
        s.add(w[i:j+1])
print(len(s))
# print(sorted(list(s)))