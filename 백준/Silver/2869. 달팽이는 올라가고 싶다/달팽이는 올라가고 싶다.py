import math
a, b, v = map(int, input().split()) # 아침, 저녁 높이
dalpang = 0
day = 0

day = (v-b)/(a-b)
print(math.ceil(day))