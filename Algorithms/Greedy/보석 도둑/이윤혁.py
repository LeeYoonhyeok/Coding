'''
가방에 담을 수 있는 최대 보석의 가격 합 구하기
가방에는 보석을 하나만 담을 수 있음
'''

import heapq
import sys

N, K = map(int, sys.stdin.readline().split())
jewels = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bags = [int(sys.stdin.readline()) for _ in range(K)]
heap = []
ans = 0
ind = 0

jewels.sort(key = lambda x:x[0])
bags.sort()

for bag in bags:
    while ind < N and jewels[ind][0] <= bag:
        heapq.heappush(heap, -jewels[ind][1])
        ind += 1
        
    if heap:
        ans += -heapq.heappop(heap)

print(ans)