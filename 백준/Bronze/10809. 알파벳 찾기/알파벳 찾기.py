w = list(input())

a = (ord('z') - ord('a'))
cnt = [-1] * (a + 1)

for i in range(len(w)):
    n = ord(w[i])
    if cnt[ord(w[i]) - 97] == -1:
        cnt[ord(w[i]) - 97] = i

print(*cnt)