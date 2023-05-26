def solution(phone_book):
    a = phone_book
    a.sort()
    for i in range(len(a)-1):
        now, nxt = a[i],a[i+1]
        if now == nxt[:len(now)]:
            return False
    return True
    