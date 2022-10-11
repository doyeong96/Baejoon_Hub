cro_alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
cnt = 0

for i in cro_alp:
    if word.count(i):
        cnt += word.count(i)

print(len(word) - cnt)