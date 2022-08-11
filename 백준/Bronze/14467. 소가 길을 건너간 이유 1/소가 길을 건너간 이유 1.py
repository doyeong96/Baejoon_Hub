look = int(input()) # 소 관찰횟수

cow_list = [2]*11
cnt = 0

for _ in range(look):
    cownum, cowdir = map(int, input().split())

    if cow_list[cownum] == 2:
        cow_list[cownum] = cowdir
    else:
        if cow_list[cownum] != cowdir:
            cnt += 1
            cow_list[cownum] = cowdir

print(cnt)