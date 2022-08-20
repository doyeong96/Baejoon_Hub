word = input()
word_dic = {}
word = word.lower()
word = list(word)
n = len(word)
for i in word:
    if i in word_dic:
        word_dic[i] += 1
    else:
        word_dic[i] = 1
vL = []
cnt = 0
for v in word_dic.values():
    vL.append(v)
for j in range(len(vL)):
    if vL[j] == max(vL):
        cnt += 1
# print(cnt)
for key, val in word_dic.items():
    if val == max(word_dic.values()) and cnt <= 1:
        print(key.upper())
        break
    elif cnt >= 2:
        print('?')
        break