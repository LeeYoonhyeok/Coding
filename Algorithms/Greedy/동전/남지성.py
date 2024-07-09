import sys

n, k = map(int, sys.stdin.readline().split())
coin_v = [int(sys.stdin.readline()) for _ in range(n)]

def how_many(n, k, coin_v):
    count = 0
    coin_v.sort(reverse = True)

    for coin in coin_v:
        if k == 0:
            break
        else:
            nums = k // coin
            count += nums
            k -= nums * coin
    
    return count

print(how_many(n, k, coin_v))
