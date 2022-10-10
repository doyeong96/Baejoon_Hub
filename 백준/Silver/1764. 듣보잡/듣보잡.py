n, m = map(int, input().split())
p = [input() for _ in range(n+m)]

dut = set(p[:n])
bo = set(p[n:])
dutbo = dut & bo

print(len(dutbo))
dutbo = list(dutbo)
dutbo.sort()
for i in dutbo:
    print(i)