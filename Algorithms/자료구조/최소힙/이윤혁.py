import sys
import heapq
input = sys.stdin.readline

n = int(input())
numbers = []

for _ in range(n):
    x = int(input())
    if x == 0: # 가장 작은 값 출력
        if numbers:
            print(heapq.heappop(numbers))
        else:
            print("0")
    elif x > 0: 
        heapq.heappush(numbers, x)        