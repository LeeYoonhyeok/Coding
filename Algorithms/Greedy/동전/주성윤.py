# 동전이 N 종류
# 가치의 합을 k로 만든다!
# n은 1~10 K 는 1부터 1억
# 둘째줄부터 N개의 줄에 동전의 가치가 오름차순으로 쭉 주어진다
# 필요한 동전 개수의 최솟값을 구하자.

# k가 타겟, 제일 큰 coin으로 먼저 

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

def mini_coin(N,K,coins):
    cnt = 0
    coins.sort(reverse=True)
    for coin in coins:
        if K == 0:
            break
        cnt += K // coin
        K %= coin
    return cnt

mini_coin(N,K,coins)