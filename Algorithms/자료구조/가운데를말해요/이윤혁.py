import heapq
import sys

input = sys.stdin.readline
N = int(input())
data = [int(input()) for _ in range(N)]

max_heap = [] # 최대 힙 (음수로 저장)
min_heap = [] # 최소 힙
result = []

for i in range(N):
    num = int(data[i])
    
    # 최대 힙에 추가 (음수로 저장)
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)
    
    # 최대 힙의 최대값이 최소 힙의 최소값보다 크다면 교환
    if min_heap and -max_heap[0] > min_heap[0]:
        max_val = -heapq.heappop(max_heap)
        min_val = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -min_val)
        heapq.heappush(min_heap, max_val)
    
    # 최대 힙의 루트를 결과로 저장
    result.append(-max_heap[0])

# 결과 출력
print("\n".join(map(str, result)))
