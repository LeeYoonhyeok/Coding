import heapq
import sys
input = sys.stdin.readline

n = int(input())
numbers = []
for _ in range(n):
    x = int(input())
    if x == 0: # 최대값 출력
        if numbers:
            print(-heapq.heappop(numbers))
        else:
            print("0")
            
    else:
        heapq.heappush(numbers, -x)