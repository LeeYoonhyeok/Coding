'''
큰 동전부터 하나씩 나눠가면서 몫을 더해가면 답이 된다.

'''
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

cnt = 0
for i in range(N-1, -1, -1):
    share = int(K/coins[i])
    K = int(K%coins[i])
    
    cnt += share

print(cnt)
