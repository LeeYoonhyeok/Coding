import heapq
import sys

N = int(sys.stdin.readline())
cards = [int(sys.stdin.readline()) for _ in range(N)]
heapq.heapify(cards)
ans = 0

while len(cards) > 1:
    first = heapq.heappop(cards)
    second = heapq.heappop(cards)
    temp = first + second
    
    ans += temp
    heapq.heappush(cards, temp)
    
print(ans)
    
    
    