'''
graph를 만들어 연결고리 생성, indgree로 진입차수 생성 (위상정렬)
진입차수를 생성하여 순서를 파악해야함. 해당 건물을 진입하기에 몇 개의 건물을 지어야 하는지
'''
import sys
from collections import deque

def acm_craft(N, K, times, rules, W):
    graph = [[] for _ in range(N+1)]
    indegree = [0] * (N+1) # 진입차수
    dp = [0] * (N+1)    
    times = [0] + times
    
    for x, y in rules:
        graph[x].append(y)
        indegree[y] += 1
            
    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0: # 진입차수 = 0 -> 시작지점
            q.append(i)
            dp[i] = times[i]
    
    while q:
        current = q.popleft()
        
        for next in graph[current]:
            indegree[next] -= 1
            dp[next] = max(dp[next], dp[current] + times[next])
            
            if indegree[next] == 0:
                q.append(next)
                
    return dp[W]
            
    
tc = int(sys.stdin.readline())
for _ in range(tc):
    N, K = map(int, sys.stdin.readline().split()) # N:건물수, K:규칙수
    times = list(map(int, sys.stdin.readline().split()))
    rules = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]    
    W = int(sys.stdin.readline())
    print(acm_craft(N, K, times, rules, W))
