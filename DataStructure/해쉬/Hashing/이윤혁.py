import sys
n = int(sys.stdin.readline())
st = sys.stdin.readline()
ans = 0

for i in range(n):
    ans += (ord(st[i])-96) * (31 ** i)
    ans %= 1234567891
print(ans)