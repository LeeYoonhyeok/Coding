'''
in_degree로 진입차수 설정
heapq로 문제 번호를 작은 순서로 정렬해야 하는 요구사항 해결
heapq로 진입 차수가 0이 된 노드들 중, 가장 번호가 작은 문제를 효율적으로 선택 가능
'''

import heapq
from collections import defaultdict, deque

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = defaultdict(list)
in_degree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1
    
priority_queue = []
for i in range(1, n+1):
    if in_degree[i] == 0:
        heapq.heappush(priority_queue, i)
        
        
ans = []
while priority_queue:
    cur = heapq.heappop(priority_queue)
    ans.append(cur)
    for neighbor in graph[cur]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            heapq.heappush(priority_queue, neighbor)
            
            
print(*ans)